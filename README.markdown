kc: A command-line tool for keepalived.conf.
==================

kc is a command-line tool for manipulating keepalived.conf.


Requirements
------------------
If you want to install kc from source code, it requires following packages:

- [text-keepalived](http://github.com/maoe/kc)
- [cmdargs](http://hackage.haskell.org/package/cmdargs)
- [mtl](http://hackage.haskell.org/package/mtl)


Installation
------------------
### Binary Releases
Donwload the latest kc RPM from the github [downloads page](http://github.com/maoe/kc/downloads).

### Install from source code
You can configure, build, and install all in the usual way with Cabal:

    runhaskell Setup.hs configure
    runhaskell Setup.hs build
    runhaskell Setup.hs install


Usage
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
