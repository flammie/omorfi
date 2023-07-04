/**
 * @file omorfi.hh
 *
 * @brief Omorfi bindings for C++.
 *
 * @author Tommi A Pirinen
 */

//  This program is free software: you can redistribute it and/or modify
//  it under the terms of the GNU General Public License as published by
//  the Free Software Foundation, version 3 of the License.
//
//  This program is distributed in the hope that it will be useful,
//  but WITHOUT ANY WARRANTY; without even the implied warranty of
//  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//  GNU General Public License for more details.
//
//  You should have received a copy of the GNU General Public License
//  along with this program.  If not, see <http://www.gnu.org/licenses/>.

#ifndef _OMORFI_HH
#define _OMORFI_HH 1

#ifdef HAVE_CONFIG_H
#include <config.h>
#endif

#include <hfst/hfst.h>

/**
 * Namespace for omorfi stuff.
 */
namespace omorfi
{

/**
 * An object that can load and use omorfi language models.
 */
class Omorfi
{

  private:
    hfst::HfstTransducer *analyser_;
    bool can_analyse_;
    hfst::HfstTransducer *hyphenator_;
    bool can_hyphenate_;

    hfst::HfstTransducer *openHFST_(const std::string &filename);

  public:
    /** Construct omorfi with no models loaded. */
    Omorfi();

    /** Destroy omorfi and unload all models. */
    ~Omorfi();

    /**
     * load analysis model from a file.
     *
     * @param filename path to an automaton file binary.
     */
    void loadAnalyser(const std::string &filename);

    /**
     * load hyphenation model from a file.
     *
     * @param filename path to an automaton file binary.
     */
    void loadHyphenator(const std::string &filename);

    /**
     * analyse a string as a single input token.
     *
     * @param token  word to analys as string
     *
     * @return an unordered vector of strings giving all known analyses. May
     * be an empty list if no analyses are found, but this behaviour cannot
     * be trusted upon: many models will back-off giving at least one analysis
     * for any given input.
     */
    std::vector<std::string> analyse(const std::string &token);

    /**
     * hyphenate a string as a single input token.
     *
     * @param token  word to analys as string
     *
     * @return an unordered vector of strings giving all known hyphenations.
     * May be an empty list if no analyses are found, but this behaviour
     * cannot be trusted upon: many models will back-off giving at least one
     * hyphrnation for any given input.
     */
    std::vector<std::string> hyphenate(const std::string &token);

    /**
     * tokenise a string for analysis.
     *
     * @param text  text to split into tokens.
     *
     * @return a vector of tokens given as strings, in order they should
     * appear in the analyses. The return value does not need to be a
     * split of  source @c text.
     */
    std::vector<std::string> tokenise(const std::string &text);

    /**
     * Test if string is a valid word-form and in the lexicon.
     * Note that this function is not any faster than @c analyse, but it
     * resolves some internal codings of guessed analyses.
     *
     * @param token  a word to test
     * @return true if token is in dictionary, false otherwise
     */
    bool accept(const std::string &token);
};

}

#endif // OMORFI_HH
