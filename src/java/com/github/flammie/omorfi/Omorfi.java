/**
 * @file Omorfi.java
 * @brief Simple java interface for omorfi using hfst optimised lookup java.
 *
 * Consider this as a standard java interface to omorfi and standard reference
 * for scientific research as far as java is concerned.
 *
 */

package com.github.flammie.omorfi;

import java.io.File;
import java.io.FileInputStream;
import java.io.DataInputStream;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Collection;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

import net.sf.hfst.Transducer;
import net.sf.hfst.TransducerHeader;
import net.sf.hfst.TransducerAlphabet;
import net.sf.hfst.UnweightedTransducer;
import net.sf.hfst.WeightedTransducer;
import net.sf.hfst.NoTokenizationException;

/**
 * @brief An object holding automata for all functions of omorfi.
 *
 * Each of the automata are accessible by their function and identifier.
 * Some combinations of functionalities may be available that access more
 * than one automaton in non-trivial ways. Currently supported automata
 * functions are:
 *   * analysis
 *   * tokenisation
 *   * generation
 *   * lemmatisation
 *   * segmentation
 *   * lookup
 * These are followed by corresponding automaton sets as attributes:
 *       analysers: key is 'omorfi-' + tagset
 *       tokenisers: key is 'omorfi'
 *       generators: key is 'omorfi-' + tagset
 *       lemmatizers: key is 'omorfi'
 *       hyphenators: key is 'omorfi'
 *       segmenters: key is 'omorfi'
 *
 * The java code can perform minimal string munging.
 */
public class Omorfi
{

    /**
     * @brief construct empty omorfi holder.
     */
    public Omorfi()
    {
        lowercase = true;
        uppercase = true;
        titlecase = true;
        analysers = new HashMap<String, Transducer>();
        tokenisers = new HashMap<String, Transducer>();
        lemmatisers = new HashMap<String, Transducer>();
        generators = new HashMap<String, Transducer>();
        hyphenators = new HashMap<String, Transducer>();
        acceptors = new HashMap<String, Transducer>();
        segmenters = new HashMap<String, Transducer>();
    }

    static private Transducer loadTransducer(String path) 
        throws java.io.FileNotFoundException, java.io.IOException,
                          net.sf.hfst.FormatException
    {
        FileInputStream transducerfile = new FileInputStream(path);
        TransducerHeader h = new TransducerHeader(transducerfile);
        DataInputStream charstream = new DataInputStream(transducerfile);
        TransducerAlphabet a = new TransducerAlphabet(charstream,
                h.getSymbolCount());
        if (h.isWeighted())
        {
            return new WeightedTransducer(transducerfile,
                    h, a);
        }
        else
        {
            return new UnweightedTransducer(transducerfile,
                    h, a);
        }
    }

    /**
     * @brief Load omorfi automaton from filename and guess its use.
     *
     * A file name should consist of three parts separated by full stop.
     * The second part must be a keyword describing the use of the
     * automaton, first part is parsed as an identifier typically starting
     * with the word omorfi, followed by any extras, such as the tagset for
     * analysis or generation.
     */
    public void load(String path) throws java.io.FileNotFoundException,
           java.io.IOException, net.sf.hfst.FormatException
    {
        String filename = path.substring(path.lastIndexOf("/") + 1);
        System.out.println(filename);
        String id = filename.substring(0, filename.indexOf("."));
        if (filename.indexOf(".") == filename.lastIndexOf("."))
        {
            return;
        }
        String type = filename.substring(filename.indexOf(".") + 1, 
                filename.lastIndexOf("."));
        if ((!type.equals("analyse")) && (!type.equals("generate")) &&
                (!type.equals("accept")) && (!type.equals("tokenise")) &&
                (!type.equals("lemmatise")) && (!type.equals("segment")))
        {
            System.out.println(filename + ": Unrecognised type " + type);
            return;
        }
        if (type.equals("analyse"))
        {
            System.out.println(filename + " = " + type + " : " + id);
            analysers.put(id, loadTransducer(path));
        }
/*        else if (type.equals("generate"))
        {
            generators.put(id, loadTransducer(path));
        }
        else if (type.equals("accept"))
        {
            acceptors.put(id, loadTransducer(path));
        }
        else if (type.equals("tokenise"))
        {
            tokenisers.put(id, loadTransducer(path));
        }
        else if (type.equals("lemmatise"))
        {
            lemmatisers.put(id, loadTransducer(path));
        }
        else if (type.equals("hyphenate"))
        {
            hyphenators.put(id, loadTransducer(path));
        }
        else if (type.equals("segment"))
        {
            segmenters.put(id, loadTransducer(path));
        }
*/        else
        {
            System.out.println(filename + ": Unrecognised type " + type);
        }
    }

    /**
     * @brief load all recognisable automata in given path.
     */
    public void loadAll(String path) throws java.io.FileNotFoundException,
           java.io.IOException
    {
        File dir = new File(path);
        if (!dir.exists())
        {
            throw new java.io.FileNotFoundException();
        }
        File[] files = dir.listFiles();
        for (File file : files)
        {
            if (file.toString().matches(".*\\.hfst$"))
            {
                try
                {
                    load(file.toString());
                }
                catch (net.sf.hfst.FormatException fe)
                {
                    // pass
                    System.out.println(file + ":" + fe);
                }
            }
        }
    }

    /**
     * @brief load all automata in standard system locations.
     */
    public void loadAll() throws java.io.FileNotFoundException,
           java.io.IOException
    {
        List<String> stdpaths = new ArrayList<String>();
        stdpaths.add("/usr/local/share/hfst/fi/");
        stdpaths.add("/usr/share/hfst/fi/");
        stdpaths.add("/usr/local/share/omorfi/");
        stdpaths.add("/usr/share/omorfi/");
        if (System.getenv("HOME") != null)
        {
            stdpaths.add(System.getenv("HOME") + "/.hfst/fi/");
            stdpaths.add(System.getenv("HOME") + "/.omorfi/");
        }
        for (String path : stdpaths)
        {
            System.out.println("Loading " + path);
            try {
                loadAll(path);
            }
            catch (java.io.FileNotFoundException fnfe)
            {
                // pass
            }
        }
    }

    /**
      * @brief Perform a simple morphological analysis lookup.
      *
      * If can_titlecase does not evaluate to False,
      * the analysis will also be performed with first letter
      * uppercased and rest lowercased.
      * If can_uppercase evaluates to not False,
      * the analysis will also be performed on all uppercase variant.
      * If can_lowercase evaluates to not False,
      * the analysis will also be performed on all lowercase variant.
      * 
      * The analyses with case mangling will have an additional element to them
      * identifying the casing.
      */
    public Collection<String> analyse(String wf, String automaton) throws net.sf.hfst.NoTokenizationException
    {
        System.out.println("Analysing " + wf + " with " + automaton);
        Collection<String> res = analysers.get(automaton).analyze(wf);
        if (uppercase)
        {
            Collection<String> upres =
                analysers.get(automaton).analyze(wf.toUpperCase());
            for (String s : upres)
            {
                s = s + "[CASECHANGE=UPPERCASED]";
            }
            res.addAll(upres);
        }
        if (lowercase)
        {
            Collection<String> lowres =
                analysers.get(automaton).analyze(wf.toLowerCase());
            for (String s : lowres)
            {
                s = s + "[CASECHANGE=LOWERCASED]";
            }
            res.addAll(lowres);
        }
        for (String s : res)
        {
            s.replace("\t", "[WEIGHT=").replace("$", "]");
        }
        return res;
    }

    /**
     * @brief perform analysis with any loaded automaton.
     */
    public Collection<String> analyse(String wf) throws net.sf.hfst.NoTokenizationException
    {
        System.out.println("Analysing " + wf);
        System.out.println(analysers);
        Collection<String> anals = new ArrayList<String>();
        if (analysers.containsKey("default"))
        {
            anals = analyse(wf, "default");
        }
        if ((anals.size() == 0) && (analysers.containsKey("omorfi-omor")))
        {
            anals = analyse(wf, "omorfi-omor");
        }
        if (anals.size() == 0)
        {
            anals = new ArrayList<String>();
            anals.add("[WORD_ID=" + wf + "][GUESS=UNKNOWN][WEIGHT=inf]");
        }
        return anals;
    }

    /**
     * @brief Perform tokenisation with specific automaton.
     */
    public Collection<String> tokenise(String line, String id)
    {
        return new ArrayList<String>();
    }

    /**
      * @brief Perform tokenisation with loaded tokeniser if any, or split.
      *
      * If tokeniser is available, it is applied to input line and if
      * result is achieved, it is split to tokens according to tokenisation
      * strategy and returned as a list.
      *
      * If no tokeniser are present, or none give results, the line will be
      * tokenised using java's basic string functions.
      */
    public Collection<String> tokenise(String line)
    {
        Collection<String> tokens = new ArrayList<String>();
        try
        {
            if (tokenisers.containsKey("omorfi"))
            {
                tokens = tokenise(line, "omorfi");
            }
        }
        catch (NullPointerException npe)
        {
            // pass
        }
        if (tokens.size() == 0)
        {
            tokens = new ArrayList<String>();
            for (String token : line.replace(".", " .").split(" "))
            {
                tokens.add(token);
            }
        }
        return tokens;
    }

    /** @brief analysers */
    private Map<String, Transducer> analysers;
    /** @brief tokenisers */
    private Map<String, Transducer> tokenisers;
    /** @brief lemmatisers */
    private Map<String, Transducer> lemmatisers;
    /** @brief generators */
    private Map<String, Transducer> generators;
    /** @brief hyphenators */
    private Map<String, Transducer> hyphenators;
    /** @brief acceptors */
    private Map<String, Transducer> acceptors;
    /** @brief segmenters */
    private Map<String, Transducer> segmenters;
    /** @brief whether try uppercasing */
    private boolean uppercase;
    /** @brief whether try untitlecasing */
    private boolean titlecase;
    /** @brief whether try lowercasing */
    private boolean lowercase;


    /**
     * @brief example CLI analysis app.
     */
    public static void main(String[] args)
    {
        Omorfi omorfi = new Omorfi();
        try
        {
            System.out.println("Reading all in system locations");
            omorfi.loadAll();
            System.out.println("Read all.");
        }
        catch (java.io.FileNotFoundException fnfe)
        {
            fnfe.printStackTrace(System.out);
        }
        catch (java.io.IOException ioe)
        {
            ioe.printStackTrace(System.out);
        }
        BufferedReader br = new BufferedReader(
                new InputStreamReader(System.in));
        String line;
        try
        {
            System.out.print("> ");
            System.out.flush();
            while ((line = br.readLine()) != null) 
            {
                Collection<String> tokens = omorfi.tokenise(line);
                for (String token : tokens) 
                {
                    Collection<String> anals = omorfi.analyse(token);
                    for (String anal : anals)
                    {
                        System.out.println(anal);
                    }
                }
                System.out.print("> ");
            }
        }
        catch (java.io.IOException ioe)
        {
            ioe.printStackTrace(System.out);
        }
        catch (net.sf.hfst.NoTokenizationException nte)
        {
            System.out.println("NoTokenizationException");
        }
    }
}

