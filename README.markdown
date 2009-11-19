kc: A command-line tool for keepalived.conf.
==================

kc is a command-line tool for manipulating keepalived.conf.


REQUIREMENTS
------------------
haskell-keepalived package requires following packages:

- [text-keepalived](http://github.com/maoe/kc)
- [cmdargs](http://hackage.haskell.org/package/cmdargs)
- [mtl](http://hackage.haskell.org/package/mtl)


INSTALLATION
------------------
You can configure, build, and install all inthe usual way with Cabal:

    runhaskell Setup.hs configure
    runhaskell Setup.hs build
    runhaskell Setup.hs install


USAGE
------------------
    kc verify [FLAG] [FILE]
      Verify configuration files.

    kc dump [FLAG] [FILE]
      Dump configuration files.

    Common flags:
      -? --help[=FORMAT]  Show usage information (optional format)
      -V --version        Show version information
      -v --verbose        Higher verbosity
      -q --quiet          Lower verbosity


[1]: http://hackage.haskell.org/
