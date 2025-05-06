SHELL=/bin/zsh

.PHONY: activate-env
activate-env:
	@echo "Activating the virtual environment"
	@. .env/bin/activate

.PHONY: build
build: activate-env
	@echo "Building a run as an app"
	@python3 setup.py py2app

.PHONY: install
install: build
	@echo "Installing the app"
	@rm -rf /Applications/notibar.app
	@mv dist/*.app /Applications
	@echo "App installed in /Applications"