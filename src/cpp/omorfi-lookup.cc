/**
 * @file omorfi-lookup.cc
 *
 * @brief Example demo of omorfi C++ API usage.
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


#include <getopt.h>

#include "omorfi.hh"

/** Print standard usage message.
 *
 * @param program_name name of the program
 */
void
print_usage(const char* program_name) {
    // c.f. http://www.gnu.org/prep/standards/standards.html#g_t_002d_002dhelp
    // Usage line
    printf("Usage: %s [OPTIONS...] FSAFILE\n"
           "Lookup tokens using omorfi\n"
        "\n", program_name);
    printf("  -h, --help      print this help\n");
    printf("  -V, --version   show version info\n");
    printf("\n");
}

/** Command-line interface to omorfi lookup.
 *
 * @param argc  number of arguments
 * @param argv  arguments in array
 * @return 0 if program terminated succesfully, 1 otherwise
 */
int main(int argc, char** argv) {
    while (true) {
        static const struct option long_options[] = {
              {"help", no_argument, 0, 'h'},
              {"version", no_argument, 0, 'V'},
              {0,0,0,0}
        };
        int option_index = 0;
        int c = getopt_long(argc, argv, "hV", long_options, &option_index);
        if (-1 == c) {
            break;
        }
        switch (c) {
          case 'h':
            print_usage(argv[0]);
            exit(0);
            break;
          case 'V':
            printf("%s\n", PACKAGE_STRING);
            exit(0);
            break;
          case '?':
          case ':':
          default:
            printf("Some error in getopt handling, maybe -%c\n", optopt);
            break;
        }
    }
    if ((argc - optind) == 1) {
        std::string fsafilename(argv[optind]);
        printf("Opening %s for omorfi\n", fsafilename.c_str());
        omorfi::Omorfi omorfi;
        try {
            omorfi.loadAnalyser(fsafilename);
        } catch(TransducerHasWrongTypeException& thwte) {
            printf("%s was not an omorfi analyser automaton binary\n",
                   fsafilename.c_str());
            exit(1);
        } catch(NotTransducerStreamException& thwte) {
            printf("%s was not an omorfi analyser automaton binary\n",
                   fsafilename.c_str());
            exit(1);
        }
        printf("Reading one token per line:\n");
        char* line = nullptr;
        size_t len = 0;
        ssize_t read;
        while ((read = getline(&line, &len, stdin)) != -1) {
            std::string token(line);
            // getline includes \n; should never have more than one \n
            if (token.find("\n") != string::npos) {
                token = token.substr(0, token.rfind("\n"));
            }
            std::vector<std::string> analyses = omorfi.analyse(token);
            printf("→ %s:\n", token.c_str());
            for (std::string analysis : analyses) {
                printf("← %s\n", analysis.c_str());
            }
        }
    } else {
        printf("Exactly one FSAFILE argument is needed\n");
        exit(1);
    }
}



