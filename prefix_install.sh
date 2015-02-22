
export EPREFIX=/lustre4/home/oogasawa/gentoo
wget http://rsync.prefix.bitzolder.nl/scripts/bootstrap-prefix.sh
chmod +x bootstrap-prefix.sh
unset PERL5LIB
unset PERL_MB_OPT
unset PERL_LOCAL_LIB_ROOT
unset PERL_MM_OPT
#unset LD_LIBRARY_PATH
#unset LIBRARY_PATH
export LANG=C

export PATH=$EPREFIX/usr/bin:$EPREFIX/bin:$EPREFIX/tmp/usr/bin:$EPREFIX:/tmp/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/bin:/sbin
./bootstrap-prefix.sh $EPREFIX stage1 2>&1 | tee stage1.log
./bootstrap-prefix.sh $EPREFIX stage2 2>&1 | tee stage2.log
./bootstrap-prefix.sh $EPREFIX stage3 2>&1 | tee stage3.log
cd $EPREFIX
hash -r
emerge -e system 2>&1 | tee emerge_e_syetem.log
emerge --sync    2>&1 | tee emerge_sync.log
./bootstrap-prefix.sh $EPREFIX startscript
