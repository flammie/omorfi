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

import net.sf.hfst.Transducer;
import net.sf.hfst.TransducerHeader;
import net.sf.hfst.TransducerAlphabet;
import net.sf.hfst.UnweightedTransducer;
import net.sf.hfst.WeightedTransducer;
import net.sf.hfst.NoTokenizationException;

/**
 * @brief An object holding automata for all functions of omorfi.
 *
 * Currently supported automata functions are:
 *   * analysis
 *   * tokenisation
 *   * generation
 *   * lemmatisation
 *   * segmentation
 *   * lookup
 *
 * The java code can perform minimal string munging by tokenisation, recasing.
 */
public class Omorfi
{

    /** @brief analyser */
    private Transducer analyser;
    /** @brief tokeniser */
    private Transducer tokeniser;
    /** @brief lemmatiser */
    private Transducer lemmatiser;
    /** @brief generator */
    private Transducer generator;
    /** @brief hyphenator */
    private Transducer hyphenator;
    /** @brief acceptor */
    private Transducer acceptor;
    /** @brief segmenter */
    private Transducer segmenter;
    /** @brief whether try uppercasing */
    private boolean uppercase;
    /** @brief whether try titlecasing */
    private boolean titlecase;
    /** @brief whether try lowercasing */
    private boolean lowercase;
    /** @brief whether try untitlecasing */
    private boolean detitlecase;


    /**
     * @brief construct empty omorfi holder.
     */
    public Omorfi()
    {
        lowercase = true;
        uppercase = true;
        titlecase = true;
        detitlecase = true;
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

    public void loadAnalyser(String path) throws java.io.FileNotFoundException,
           java.io.IOException, net.sf.hfst.FormatException
    {
        analyser = loadTransducer(path);
    }

    /**
     * @brief Load omorfi automaton from filename and guess its use.
     *
     * A file name should consist of three parts separated by full stop.
     * The second part must be a keyword describing the use of the
     * automaton, first part must be "omorfi".
     *
     * @deprecated use loadXXX(String) versions instead
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
        else if (!id.equals("omorfi"))
        {
            return;
        }
        String type = filename.substring(filename.indexOf(".") + 1,
                filename.lastIndexOf("."));
        if ((!type.equals("analyse")) && (!type.equals("generate")) &&
                (!type.equals("accept")) && (!type.equals("tokenise")) &&
                (!type.equals("lemmatise")) && (!type.equals("segment")) &&
                (!type.equals("describe")))
        {
            System.out.println(filename + ": Unrecognised type " + type);
            return;
        }
        if (type.equals("analyse") || type.equals("describe"))
        {
            System.out.println(filename + " = " + type + " : " + id);
            analyser = loadTransducer(path);
        }
        else if (type.equals("generate"))
        {
            generator = loadTransducer(path);
        }
        else if (type.equals("accept"))
        {
            acceptor = loadTransducer(path);
        }
        else if (type.equals("tokenise"))
        {
            tokeniser = loadTransducer(path);
        }
        else if (type.equals("lemmatise"))
        {
            lemmatiser = loadTransducer(path);
        }
        else if (type.equals("hyphenate"))
        {
            hyphenator = loadTransducer(path);
        }
        else if (type.equals("segment"))
        {
            segmenter = loadTransducer(path);
        }
        else
        {
            System.out.println(filename + ": Unrecognised type " + type);
        }
    }

    /**
     * @brief load all recognisable automata in given path.
     *
     * @deprecated use loadXXX(String) versions instead
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
     *
     * @deprecated use loadXXX(String) versions instead
     */
    public void loadAll() throws java.io.FileNotFoundException,
           java.io.IOException
    {
        List<String> stdpaths = new ArrayList<String>();
        stdpaths.add("/usr/local/share/omorfi/");
        stdpaths.add("/usr/share/omorfi/");
        if (System.getenv("HOME") != null)
        {
            stdpaths.add(System.getenv("HOME") + "/.omorfi/");
        }
        stdpaths.add("./");
        stdpaths.add("generated/");
        stdpaths.add("src/generated/");
        stdpaths.add("../src/generated/");
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
    public Collection<String> analyse(String wf) throws net.sf.hfst.NoTokenizationException
    {
        System.out.println("Analysing " + wf);
        Collection<String> res = new ArrayList<String>(
                analyser.analyze(wf));
        Collection<String> rv = new ArrayList<String>();
        for (String s : res)
        {
            rv.add(s.replace("\t", "[WEIGHT=") + "]");
        }
        if (uppercase && (!wf.equals(wf.toUpperCase())))
        {
            Collection<String> upres = new ArrayList<String>(
                analyser.analyze(wf.toUpperCase()));
            for (String s : upres)
            {
                rv.add(s.replace("\t", "[WEIGHT=") +
                    "][CASECHANGE=UPPERCASED]");
            }
        }
        if (lowercase && (!wf.equals(wf.toLowerCase())))
        {
            Collection<String> lowres = new ArrayList<String>(
                analyser.analyze(wf.toLowerCase()));
            for (String s : lowres)
            {
                rv.add(s.replace("\t", "[WEIGHT=") +
                        "][CASECHANGE=LOWERCASED]");
            }
        }
        if (rv.size() == 0) {
            rv.add("[WORD_ID=" + wf +
                    "][UPOS=NOUN][NUM=SG][CASE=NOM][GUESS=HEUR][WEIGHT=65536]");
        }
        return rv;
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

