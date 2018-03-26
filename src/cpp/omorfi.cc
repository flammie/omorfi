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
#include <dirent.h>

#include "omorfi.hh"

namespace omorfi {

    Omorfi::Omorfi() :
        can_analyse_(false)
    {}

    Omorfi::~Omorfi() {
        if (analyser_ != nullptr) {
            delete analyser_;
        }
    }

    void
    Omorfi::loadAllFromDefaultDirs() {
        std::vector<std::string> stdPaths = {"/usr/local/share/omorfi/",
            "/usr/share/omorfi/"};
        char* homepath = getenv("HOME");
        if (homepath != nullptr) {
            std::string homeomorfi = string(homepath) + "/.omorfi/";
            stdPaths.push_back(homeomorfi);
        }
        for (auto path : stdPaths) {
            DIR* dirp = opendir(path.c_str());
            if (dirp != nullptr) {
                loadFromDir(path);
            }
        }
    }

    void
    Omorfi::loadFromDir(const std::string& dirname) {
        glob_t* globs;
#ifdef GLOB_TILDE
        glob((dirname + "/omorfi*.hfst").c_str(), GLOB_TILDE, nullptr,
             globs);
#else
	if (dirname[0] == '~')
            fprintf(stderr,
                    "GLOB_TILDE is not supported on your platform, "
                    "the tilde in \"%s\" won't be expanded.",
                    dirname.c_str());

        glob((dirname + "/omorfi*.hfst").c_str(), 0, nullptr, globs);
#endif
        for (unsigned int i = 0; i < globs->gl_pathc; i++) {
            std::string filepath(globs->gl_pathv[1]);
            loadFile(filepath);
        }
        globfree(globs);
    }

    void
    Omorfi::loadFile(const std::string& filename) {
        if (filename.find(".analyse.")) {
            loadAnalyser(filename);
        }
        else {
            fprintf(stderr, "Unrecognised automaton %s", filename.c_str());
        }
    }

    hfst::HfstTransducer*
    Omorfi::openHFST_(const std::string& path) {
        hfst::HfstInputStream his(path);
        //his.open();
        hfst::HfstTransducer* hfst = new hfst::HfstTransducer(his);
        his.close();
        return hfst;
    }

    void
    Omorfi::loadAnalyser(const std::string& filename) {
          analyser_ = openHFST_(filename);
          if (analyser_ != nullptr) {
              can_analyse_ = true;
          } else {
              can_analyse_ = false;
          }
    }

    std::vector<std::string>
    Omorfi::analyse(const std::string& token) {
        std::vector<std::string> anals;
        if (can_analyse_) {
            // do it
            hfst::HfstOneLevelPaths* results = analyser_->lookup_fd(token);
            for (hfst::HfstOneLevelPath anal : *results) {
                hfst::StringVector analysis = anal.second;
                std::string a;
                for (std::string c : analysis) {
                    a += c;
                }
                anals.push_back(a);
            }
            return anals;
        } else {
            // XXX: error
            throw std::runtime_error("analyser not loaded");
        }
        return std::vector<std::string>();
     }

     std::vector<std::string>
     Omorfi::tokenise(const std::string& /* text */) {
         return std::vector<std::string>();
     }

     bool
     Omorfi::accept(const std::string& token) {
         return (analyse(token).size() > 0);
     }



}


