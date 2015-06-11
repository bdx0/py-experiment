#!/bin/bash -
# An install file for ATLAS SSE2-only build on 64-bit Windows
#
# Must be unix line endings
# In vim - set ff=unix
# Turn off CPU throttling
# Control panel, Hardware and sound, Power options, Select a power plan, Show
# additional plans, High perfornamce
win_home=$(pwd)
downloads="${win_home}"
code_home="${win_home}"

atlas_ver="3.10.1"
build_suff="-64-full-sse2"
# usually don't need to change these guys
atlas_home="${code_home}/atlas"
atlas_sdir=atlas-${atlas_ver}
atlas_src=$atlas_home/$atlas_sdir
arch_src=$atlas_home/WINAD
atlas_build="$atlas_home/atlas-${atlas_ver}-build${build_suff}"
atlas_tar="${downloads}/atlas${atlas_ver}.tar.bz2"
lapack_tarfile="${win_home}/lapack-3.5.0.tgz"
arch_tar="${win_home}/win64_archdef.tar"
[ -f $lapack_tarfile ] || wget http://netlib.org/lapack/lapack.tgz -O $lapack_tarfile
[ -f $atlas_tar ] || wget http://liquidtelecom.dl.sourceforge.net/project/math-atlas/Stable/3.10.1/atlas3.10.1.tar.bz2 -O $atlas_tar
[ -f $arch_tar ] || wget http://math-atlas.sourceforge.net/fixes/win64_archdef.tar -O $arch_tar


# SSE2 for 3.10.1
#config_opts="-b 64 --with-netlib-lapack-tarfile=${lapack_tarfile}"
#config_opts="-b 64 -Si nocygwin 1 --with-netlib-lapack-tarfile=${lapack_tarfile} -Ss ADdir $arch_src"
#config_opts="-b 32  --with-netlib-lapack-tarfile=${lapack_tarfile} -Si nocygin 1 -Ss ADdir $arch_src"
#config_opts="-b 64 -Si nocywgin 1 --with-netlib-lapack-tarfile=${lapack_tarfile}"
config_opts="-v 5 -O 1 -A 13 -V 192 -b 32 -C xc,ic	`which gcc`  -D c -DWALL -t -1 -m 3000 -Si archdef 0 -Si nocygwin 0 -Si nof77 1 -Ss kern `which gcc` " 

# doit
#rm -rf $atlas_src
rm -rf $atlas_build
mkdir -p $atlas_build
# Copy this file into the build directory
if [[ -e "$0" ]]; then
    cp $0 $atlas_build
fi
cd $atlas_home
[ -d $atlas_src ]  || (tar jxvf "$atlas_tar" && mv ATLAS ${atlas_src})
#[ -d $atlas_src ] || (git clone https://github.com/vtjnash/atlas-3.10.0.git $atlas_src)
[ -d $arch_src ] || (tar xvf "$arch_tar" && mv WINAD $arch_src)
cd $atlas_build
${atlas_src}/configure ${config_opts}
read -p $(pwd)
make build
read -p "waiting something ..."