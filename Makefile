SHELL=/bin/zsh

.PHONY: activate-env
activate-env:
	@echo "Activating the virtual environment"
	@. .env/bin/activate

.PHONY: build
build:
	@echo "Building a run as an app"
	@. .env/bin/activate && python3 setup.py py2app

.PHONY: install
install: build
	@echo "Installing the app"
	@rm -rf /Applications/notibar.app
	@ls -l dist/
	@mv dist/notibar.app /Applications/Notibar.app
	@echo "App installed in /Applications"