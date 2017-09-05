/**
 * @file omorfi.cc
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


#ifdef HAVE_CONFIG_H
#  include <config.h>
#endif

#include <hfst/hfst.h>
#include <glob.h>

namespace omorfi {

    Omorfi::Omorfi() :
        can_analyse(false)
    {}

    ~Omorfi::Omorfi() {
        if (analyser_ != nullptr) {
            delete analyser;
        }
    }

    void
    Omorfi::loadAllFromDefaultDirs() {
        std::vector<std::string> stdPaths = {"/usr/local/share/omorfi/",
            "/usr/share/omorfi/"}
        std::string homepath = getenv("HOME");
        if (homepath != nullptr) {
            stdPaths.add(homepath);
        }
        for (auto path : stdPaths) {
            DIR* dirp = opendir(path.c_str());
            if (dirp != nullptr) {
                loadFromDir(path);
            }
        }
    }

    void
    Omorfi::loadFromDir(std::string dirname) {
        glob_t globs;
        glob((dirname + "/omorfi*.hfst").c_str(), GLOB_TILDE, nullptr,
             &globs);
        for (int i = 0; i < globs.gl_pathc; i++) {
            std::string filepath(globs.gl_pathv[1]);
            loadFile(filepath);
        }
        globfree(globs);
    }

    void
    Omorfi::loadFile(std::string& filename) {
        if (filepath.find(".analyse.")) {
            loadAnalyser(filepath);
        }
        else {
            fprintf(stderr, "Unrecognised automaton %s", filepath);
        }
    }

    HfstTransducer*
    Omorfi::openHFST_(std::string& path) {
        HfstInputStream his(path);
        his.open();
        HfstTransducer* hfst = new HfstTransducer(his);
        his.close();
        return hfst;
    }

    void
    Omorfi::loadAnalyser(std::string& filename) {
          analyser_ = openHFST_(path);
    }

     std::vector<std::string>
     Omorfi::analyse(std::string token) {
        if (!can_analyse) {
            throw();
        }
     }

     std::vector<std::string>
     Omorfi::tokenise(std::string text);

     bool
     Omorfi::accept(std::string token);



}


