.PHONY: env check unit_test test install run clean

env:
	virtualenv env -p /usr/bin/python3
	env/bin/python env/bin/pip install -r requirement.txt -I

install: env
	env/bin/python setup.py install

run: install
	env/bin/user_api

clean: 
	$(RM) -r .vscode
	$(RM) -r build
	$(RM) -r dist
	$(RM) -r env
	$(RM) -r *.egg-info
	$(RM) -r */__pycache__
	$(RM) -r */*.db
