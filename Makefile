### Makefile ---
## Author: dbd
## Version: 0.0.1

### Commentary:
##
##


### Code:

##
# git config --global user.email baoduy.duong0206@gmail.com
# git config --global user.name  "Duong Bao Duy"
# git config --global core.autocrlf false
# git config --global core.filemode false
# and for fun!
# git config --global color.ui true
##

LOCAL_PATH = $(dir $(realpath $(lastword $(MAKEFILE_LIST))))

script:
	mkdir ./script
	@echo Done $@ !!

script/%: script
	([ -f $@ ] && echo $@ exist) ||	touch $@
	chmod 777 $@
	@echo Done $@ !!

src:
	mkdir ./src
	@echo Done $@ !!

src/%: src
	([ -d $@ ] && echo $@ exist) || mkdir $@
	@echo Done $@ !!

targets:
	mkdir ./targets
	@echo Done $@ !!


targets/%: targets
	([ -d $@ ] && echo $@ exist) || mkdir $@
	@echo Done $@ !!

app/update.mk:
	@([ -f $@ ] && echo $@ created) || (echo Create app/update.mk to install require tools && exit 1)
	@echo Done $@ !!!

app:
	mkdir ./app
	@echo Done $@ !!

.PHONY: tool
tool:  app app/update.mk
	cd $(word 1,$^) && $(MAKE) -f update.mk
	@echo Done $@ !!

.PHONY: create
git-create: tool script
	git init
	git config --global user.name "Duong Bao Duy"
	git config --global user.email "baoduy.duong0206@gmail.com"
	case "$(shell git remote)" in \
		"origin" ) git remote remove origin ;; \
	esac
	git remote add origin https://github.com/duongbaoduy/py-experiment.git
	@echo Done $@ : $^ !!

.PHONY: build
build:
	@echo Done $@ !!

.PHONY: clean
clean:
	@echo Done $@ !!

.PHONY: all
all:
	@echo Your script path: $(LOCAL_PATH)
	@echo Select target for make
	@echo Done $@ !!!

.PHONY: pub
git-pub:
	git push -u origin --all
	@echo Done $@ !!

.PHONY: gitk
gitk:
	gitk.cmd --all
	@echo Done $@ !!

.suffixes: .c .cc .cpp .h .o .py .java
.SHELLFLAGS: -e
#.ONESHELL:
#SHELL = /usr/bin/perl
#.SHELLFLAGS = -e
# show :
#         @f = qw(a b c);
#         print "@f\n";
