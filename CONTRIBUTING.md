# Community guidelines

Omorfi is a free / libre open source community-based project. We welcome all
contributions and help wholeheartedly. Ways you can contribute:

* Coding: Improve conversions, processing, parsers, etc.
* Lexicography: information about words
* Donations: money for coffee / beer / conference fund for the main developers

Contributions accepted on github: file issues, fork and send pull requests.
Developers can be contacted on IRC: [#omorfi on
Freenode](irc://freenode/#omorfi,ischannel), [omorfi-devel mailing
 list](https://groups.google.com/forum/#!forum/omorfi-devel), or on github
platform.

## Code of conduct

See [our code of conduct](//flammie.github.io/omorfi/CODE_OF_CONDUCT.html). It
is adapted from github's suggested code of conduct.

## Licencing contributions

Any data or code contributed must be compatible with our licencing policy, i.e.
GNU compatible free licence.

## Git(hub) usage

In github, you may use the "fork this project" button to contribute, read
github's documentation for more information about this work-flow.

We are currently using
[git-flow](http://nvie.com/posts/a-successful-git-branching-model/), but feel
free to just send pull-requests as you find comfortable and we'll sort it out.

## Coding standards

Python code should pass the flake8 style checker and imports should be sorted
in accordance with isort. Ideally, you should integrate these into your editor,
[the development environment section of the python guide has instructions for a
few editors](//docs.python-guide.org/en/latest/dev/env/). In addition, you can
install a pre-commit hook to run the checks like so:

```
$ pip install pre-commit
$ pre-commit install
```

I (Flammie) also recommend using editor that supports
[editor-config](//editorconfig.org) as well as automatic syntax checking, , e.g.
I use [ale](//github.com/w0rp/ale) with [vim](//vim.org)

## Testing

It is highly recommended to run `make` and `make check` or even `make distcheck`
to test contributions to either word data or python scripts. This will also be
done by continuous integration tools on push of the commits.

## Donations

A lot of omorfi development has been done on spare time and by volunteers, if
you want to support [Flammie](https://flammie.github.io) you can use the
github's ❤️Sponsor button, or any of the services below:

<a href="https://liberapay.com/Flammie/donate"><img alt="Donate using Liberapay"
src="https://liberapay.com/assets/widgets/donate.svg"></a>

<a href="https://www.patreon.com/bePatron?u=9479606"
data-patreon-widget-type="become-patron-button">Become a Patron!</a>
