"CSC Consortium" masvfwiki: a general shared knowledge commons.

2021-02-26: Peter Kaminski, primary instigator.

2021-02-26: Notes on trials and errors of setup

1. working on 'git init' from and CL
   - all went well (got the msg about renaming 'master'; not 'main')
   - 'git remote add' was a bit off; did not understand what 'name'
     means in adding the repo
   - changed the name to 'origin'
   - then 'git push' error suggested 'set-upstream origin main'
   - but that command returned 'ERROR: Repository not found'
   - so back to square #2
   
2. clean up the directory (rm -fr .git/) and try again
   - also need to read Analytics Vidhya medium post more closely
   - all good *except* needed to create the repo on Github (doh!)
   - that didn't work becauses I accepted a license; i need to
     practice with a throwaway name (gah!)

2.1. test run with throwaway name foobar1 works as documented by AV.
   - 'git push --set-upstream origin main' worked w/ cscCommons; so
     maybe we are good to go.

