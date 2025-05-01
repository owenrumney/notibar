.PHONY: activate-env
activate-env:
	@echo "Activating the virtual environment"
	@source .env/bin/activate

.PHONY: build
build: 
	@echo "Building a run as an app"
	@python3 setup.py py2app

.PHONY: install
install: build
	@echo "Installing the app"
	@cp dist/*.app /Applications
	@echo "App installed in /Applications"