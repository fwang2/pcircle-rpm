.PHONY: dist prep

all: rpm

dist-latest:
	@if [ ! -d ~/pcircle ]; then \
	    echo "Can't find pcircle source"; \
   		exit 1; \
	fi
	(cd ~/pcircle; python setup.py sdist)

prep:
	rpmdev-setuptree
	cp -f ~/pcircle/dist/*.gz ~/rpmbuild/SOURCES

rpm:prep pcircle.spec
	echo "Building rpm"
	rpmbuild -ba pcircle.spec

