#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-ParamHelpers
Version  : 1.14
Release  : 3
URL      : https://cran.r-project.org/src/contrib/ParamHelpers_1.14.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ParamHelpers_1.14.tar.gz
Summary  : Helpers for Parameters in Black-Box Optimization, Tuning and
Group    : Development/Tools
License  : BSD-2-Clause
Requires: R-ParamHelpers-lib = %{version}-%{release}
Requires: R-BBmisc
Requires: R-backports
Requires: R-checkmate
Requires: R-fastmatch
BuildRequires : R-BBmisc
BuildRequires : R-backports
BuildRequires : R-checkmate
BuildRequires : R-fastmatch
BuildRequires : buildreq-R

%description
in black-box optimization, tuning and machine learning. Parameters can
    be described (type, constraints, defaults, etc.), combined to
    parameter sets and can in general be programmed on. A useful OptPath
    object (archive) to log function evaluations is also provided.

%package lib
Summary: lib components for the R-ParamHelpers package.
Group: Libraries

%description lib
lib components for the R-ParamHelpers package.


%prep
%setup -q -c -n ParamHelpers
cd %{_builddir}/ParamHelpers

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641069973

%install
export SOURCE_DATE_EPOCH=1641069973
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ParamHelpers
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ParamHelpers
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ParamHelpers
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc ParamHelpers || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ParamHelpers/DESCRIPTION
/usr/lib64/R/library/ParamHelpers/INDEX
/usr/lib64/R/library/ParamHelpers/LICENSE
/usr/lib64/R/library/ParamHelpers/Meta/Rd.rds
/usr/lib64/R/library/ParamHelpers/Meta/features.rds
/usr/lib64/R/library/ParamHelpers/Meta/hsearch.rds
/usr/lib64/R/library/ParamHelpers/Meta/links.rds
/usr/lib64/R/library/ParamHelpers/Meta/nsInfo.rds
/usr/lib64/R/library/ParamHelpers/Meta/package.rds
/usr/lib64/R/library/ParamHelpers/NAMESPACE
/usr/lib64/R/library/ParamHelpers/NEWS.md
/usr/lib64/R/library/ParamHelpers/R/ParamHelpers
/usr/lib64/R/library/ParamHelpers/R/ParamHelpers.rdb
/usr/lib64/R/library/ParamHelpers/R/ParamHelpers.rdx
/usr/lib64/R/library/ParamHelpers/help/AnIndex
/usr/lib64/R/library/ParamHelpers/help/ParamHelpers.rdb
/usr/lib64/R/library/ParamHelpers/help/ParamHelpers.rdx
/usr/lib64/R/library/ParamHelpers/help/aliases.rds
/usr/lib64/R/library/ParamHelpers/help/paths.rds
/usr/lib64/R/library/ParamHelpers/html/00Index.html
/usr/lib64/R/library/ParamHelpers/html/R.css
/usr/lib64/R/library/ParamHelpers/tests/run-all.R
/usr/lib64/R/library/ParamHelpers/tests/testthat/Rplots.pdf
/usr/lib64/R/library/ParamHelpers/tests/testthat/helper_zzz.R
/usr/lib64/R/library/ParamHelpers/tests/testthat/test_LearnerParam.R
/usr/lib64/R/library/ParamHelpers/tests/testthat/test_OptPath.R
/usr/lib64/R/library/ParamHelpers/tests/testthat/test_Param.R
/usr/lib64/R/library/ParamHelpers/tests/testthat/test_ParamSet.R
/usr/lib64/R/library/ParamHelpers/tests/testthat/test_cnames.R
/usr/lib64/R/library/ParamHelpers/tests/testthat/test_convertDiscrete.R
/usr/lib64/R/library/ParamHelpers/tests/testthat/test_convertParamSetToIrace.R
/usr/lib64/R/library/ParamHelpers/tests/testthat/test_dfRowToList.R
/usr/lib64/R/library/ParamHelpers/tests/testthat/test_dropParams.R
/usr/lib64/R/library/ParamHelpers/tests/testthat/test_evaluateParamExpressions.R
/usr/lib64/R/library/ParamHelpers/tests/testthat/test_filterParams.R
/usr/lib64/R/library/ParamHelpers/tests/testthat/test_forbidden.R
/usr/lib64/R/library/ParamHelpers/tests/testthat/test_generateDesign.R
/usr/lib64/R/library/ParamHelpers/tests/testthat/test_generateDesignOfDefaults.R
/usr/lib64/R/library/ParamHelpers/tests/testthat/test_generateGridDesign.R
/usr/lib64/R/library/ParamHelpers/tests/testthat/test_generateRandomDesign.R
/usr/lib64/R/library/ParamHelpers/tests/testthat/test_getDefaults.R
/usr/lib64/R/library/ParamHelpers/tests/testthat/test_getParamNr.R
/usr/lib64/R/library/ParamHelpers/tests/testthat/test_getParamTypeCounts.R
/usr/lib64/R/library/ParamHelpers/tests/testthat/test_getParamTypes.R
/usr/lib64/R/library/ParamHelpers/tests/testthat/test_getRequiredParamNames.R
/usr/lib64/R/library/ParamHelpers/tests/testthat/test_getRequirements.R
/usr/lib64/R/library/ParamHelpers/tests/testthat/test_hasExpression.R
/usr/lib64/R/library/ParamHelpers/tests/testthat/test_hasFiniteBoxConstraints.R
/usr/lib64/R/library/ParamHelpers/tests/testthat/test_hasIsType.R
/usr/lib64/R/library/ParamHelpers/tests/testthat/test_hasRequires.R
/usr/lib64/R/library/ParamHelpers/tests/testthat/test_isFeasible.R
/usr/lib64/R/library/ParamHelpers/tests/testthat/test_isSpecialValue.R
/usr/lib64/R/library/ParamHelpers/tests/testthat/test_isVector.R
/usr/lib64/R/library/ParamHelpers/tests/testthat/test_paramValueToString.R
/usr/lib64/R/library/ParamHelpers/tests/testthat/test_plotEAF.R
/usr/lib64/R/library/ParamHelpers/tests/testthat/test_plotYTrace.R
/usr/lib64/R/library/ParamHelpers/tests/testthat/test_renderOptPathPlot.R
/usr/lib64/R/library/ParamHelpers/tests/testthat/test_repairPoint.R
/usr/lib64/R/library/ParamHelpers/tests/testthat/test_sample.R
/usr/lib64/R/library/ParamHelpers/tests/testthat/test_trafo.R
/usr/lib64/R/library/ParamHelpers/tests/testthat/test_updateParVals.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/ParamHelpers/libs/ParamHelpers.so
/usr/lib64/R/library/ParamHelpers/libs/ParamHelpers.so.avx2
/usr/lib64/R/library/ParamHelpers/libs/ParamHelpers.so.avx512
