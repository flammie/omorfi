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
#  include <config.h>
#endif

#include <hfst/hfst.h>


namespace omorfi {

    class Omorfi {

    private:

      hfst::HfstTransducer* analyser_;
      bool can_analyse_;

      hfst::HfstTransducer* openHFST_(std::string& filename);

    public:

        Omorfi();

        ~Omorfi();

        void loadAllFromDefaultDirs();

        void loadFromDir(std::string& path);

        void loadFile(std::string& filename);

        void loadAnalyser(std::string& filename);

        std::vector<std::string> analyse(std::string token);

        std::vector<std::string> tokenise(std::string text);

        bool accept(std::string token);


    };

}

#endif // OMORFI_HH

