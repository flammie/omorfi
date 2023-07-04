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
#include <config.h>
#endif

#include <getopt.h>

#include "omorfi.hh"

/** Print standard usage message.
 *
 * @param program_name name of the program
 */
void
print_usage(const char *program_name)
{
    // c.f. http://www.gnu.org/prep/standards/standards.html#g_t_002d_002dhelp
    // Usage line
    printf("Usage: %s [OPTIONS...] FSAFILE\n"
           "Lookup tokens using omorfi\n"
           "\n",
           program_name);
    printf("  -a, --analyser=AFSA     loaf AFSA as analyser\n");
    printf("  -H, --hyphenator=HFSA   load HFSA as hyphenator\n");
    printf("  -h, --help              print this help\n");
    printf("  -V, --version           show version info\n");
    printf("\n");
}

/** Command-line interface to omorfi lookup.
 *
 * @param argc  number of arguments
 * @param argv  arguments in array
 * @return 0 if program terminated succesfully, 1 otherwise
 */
int
main(int argc, char **argv)
{
    char *analyserfilename = nullptr;
    char *hyphenatorfilename = nullptr;
    while (true)
    {
        static const struct option long_options[]
            = { { "analyser", required_argument, 0, 'a' },
                { "hyphenator", required_argument, 0, 'H' },
                { "help", no_argument, 0, 'h' },
                { "version", no_argument, 0, 'V' },
                { 0, 0, 0, 0 } };
        int option_index = 0;
        int c = getopt_long(argc, argv, "hVa:H:", long_options, &option_index);
        if (-1 == c)
        {
            break;
        }
        switch (c)
        {
        case 'a':
            analyserfilename = strdup(optarg);
            break;
        case 'H':
            hyphenatorfilename = strdup(optarg);
            break;
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
    if (analyserfilename != nullptr)
    {
        omorfi::Omorfi omorfi;
        printf("Reading analyser from: %s\n", analyserfilename);
        try
        {
            omorfi.loadAnalyser(analyserfilename);
        }
        catch (TransducerHasWrongTypeException &thwte)
        {
            printf("%s was not an omorfi automaton binary\n",
                   analyserfilename);
            exit(1);
        }
        catch (NotTransducerStreamException &thwte)
        {
            printf("%s was not an omorfi automaton binary\n",
                   analyserfilename);
            exit(1);
        }
        free(analyserfilename);
        printf("Reading one token per line:\n");
        char *line = nullptr;
        size_t len = 0;
        ssize_t read;
        while ((read = getline(&line, &len, stdin)) != -1)
        {
            std::string token(line);
            // getline includes \n; should never have more than one \n
            if (token.find("\n") != string::npos)
            {
                token = token.substr(0, token.rfind("\n"));
            }
            std::vector<std::string> analyses = omorfi.analyse(token);
            printf("→ %s:\n", token.c_str());
            for (std::string analysis : analyses)
            {
                printf("← %s\n", analysis.c_str());
            }
        }
    }
    else if (hyphenatorfilename != nullptr)
    {
        omorfi::Omorfi omorfi;
        printf("Reading hyphenator from: %s\n", hyphenatorfilename);
        try
        {
            omorfi.loadHyphenator(hyphenatorfilename);
        }
        catch (TransducerHasWrongTypeException &thwte)
        {
            printf("%s was not an omorfi automaton binary\n",
                   hyphenatorfilename);
            exit(1);
        }
        catch (NotTransducerStreamException &thwte)
        {
            printf("%s was not an omorfi automaton binary\n",
                   hyphenatorfilename);
            exit(1);
        }
        free(hyphenatorfilename);
        printf("Reading one token per line:\n");
        char *line = nullptr;
        size_t len = 0;
        ssize_t read;
        while ((read = getline(&line, &len, stdin)) != -1)
        {
            std::string token(line);
            // getline includes \n; should never have more than one \n
            if (token.find("\n") != string::npos)
            {
                token = token.substr(0, token.rfind("\n"));
            }
            std::vector<std::string> hyphens = omorfi.hyphenate(token);
            for (std::string hyphen : hyphens)
            {
                printf("-- %s\n", hyphen.c_str());
            }
        }
    }
    else if ((argc - optind) > 0)
    {
        printf("Extra parameters at the end of command line: %s...\n",
               argv[optind]);
        exit(1);
    }
    else
    {
        printf("Required -a or -H\n");
        print_usage(argv[0]);
        exit(1);
    }
}
