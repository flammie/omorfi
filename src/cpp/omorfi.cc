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
#include <config.h>
#endif

#include <algorithm>
#include <iostream>
#include <iterator>
#include <sstream>
#include <string>

#include <hfst/hfst.h>

#include "omorfi.hh"

//! timeout before libhfst gives up when traversing automata
#define OMORFI_LOOKUP_TIMEOUT 6.66f

namespace omorfi
{

Omorfi::Omorfi() : can_analyse_(false), can_hyphenate_(false) {}

Omorfi::~Omorfi()
{
    if (analyser_ != nullptr)
    {
        delete analyser_;
    }
    if (hyphenator_ != nullptr)
    {
        delete hyphenator_;
    }
}

hfst::HfstTransducer *
Omorfi::openHFST_(const std::string &path)
{
    hfst::HfstInputStream his(path);
    // his.open();
    hfst::HfstTransducer *hfst = new hfst::HfstTransducer(his);
    his.close();
    return hfst;
}

void
Omorfi::loadAnalyser(const std::string &filename)
{
    analyser_ = openHFST_(filename);
    if (analyser_ != nullptr)
    {
        can_analyse_ = true;
    }
    else
    {
        can_analyse_ = false;
    }
}

void
Omorfi::loadHyphenator(const std::string &filename)
{
    hyphenator_ = openHFST_(filename);
    if (hyphenator_ != nullptr)
    {
        can_hyphenate_ = true;
    }
    else
    {
        can_hyphenate_ = false;
    }
}

std::vector<std::string>
Omorfi::analyse(const std::string &token)
{
    std::vector<std::string> anals;
    if (can_analyse_)
    {
        // do it
        hfst::HfstOneLevelPaths *results
            = analyser_->lookup_fd(token, -1, OMORFI_LOOKUP_TIMEOUT);
        for (hfst::HfstOneLevelPath anal : *results)
        {
            hfst::StringVector analysis = anal.second;
            std::string a;
            for (std::string c : analysis)
            {
                a += c;
            }
            anals.push_back(a);
        }
        delete results;
        return anals;
    }
    else
    {
        // XXX: error
        throw std::runtime_error("analyser not loaded");
    }
    return std::vector<std::string>();
}

std::vector<std::string>
Omorfi::hyphenate(const std::string &token)
{
    std::vector<std::string> hyphens;
    if (can_hyphenate_)
    {
        // do it
        hfst::HfstOneLevelPaths *results
            = hyphenator_->lookup_fd(token, -1, OMORFI_LOOKUP_TIMEOUT);
        for (hfst::HfstOneLevelPath hyphen : *results)
        {
            hfst::StringVector analysis = hyphen.second;
            std::string a;
            for (std::string c : analysis)
            {
                if (c == "-1")
                {
                    a += "-";
                }
                else if (c == "-2")
                {
                    a += "-";
                }
                else if (c == "-3")
                {
                    a += "-";
                }
                else if (c == "-4")
                {
                    a += "-";
                }
                else
                {
                    a += c;
                }
            }
            hyphens.push_back(a);
        }
        delete results;
        return hyphens;
    }
    else
    {
        // XXX: error
        throw std::runtime_error("hyphenator not loaded");
    }
    return std::vector<std::string>();
}

std::vector<std::string>
Omorfi::tokenise(const std::string &text)
{
    std::istringstream iss(text);
    std::vector<std::string> results((std::istream_iterator<std::string>(iss)),
                                     std::istream_iterator<std::string>());
    return results;
}

bool
Omorfi::accept(const std::string &token)
{
    return (analyse(token).size() > 0);
}

}
