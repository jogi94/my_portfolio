.PHONY: clean clean-npm clean-all lint setup install help

# Default target
all: help

# SSH config entry where git needs to push. (default: portfolio-dokku)
SERVER ?= portfolio-dokku
# The name of the app. (default: portfolio)
APP ?= portfolio
# Name of the local branch. (default: develop)
BRANCH ?= develop
# Version type for bumpver. Options: [major, minor, patch]. (default: minor)
VER ?= minor

# Show this help prompt.
help:
	@ echo
	@ echo '  Usage:'
	@ echo ''
	@ echo '    make <target> [flags...]'
	@ echo ''
	@ echo '  Targets:'
	@ echo ''
	@awk '/^#/{ comment = substr($$0,3) } comment && /^[a-zA-Z][a-zA-Z0-9_-]+ ?:/{ print "   ", $$1, comment }' $(MAKEFILE_LIST) | column -t -s ':' | sort
	@echo ''
	@echo '  Flags:'
	@echo ''
	@awk '/^#/{ comment = substr($$0,3) } comment && /^[a-zA-Z][a-zA-Z0-9_-]+ ?\?=/{ print "   ", $$1, $$2, comment }' $(MAKEFILE_LIST) | column -t -s '?=' | sort
	@echo ''

# Setup command. Call: 'make APP=helpdesk-dev'
setup:
    @-git remote add deploy-$(APP) $(SERVER):$(APP)

# Install the packages needed for the application.
install:
    @pnpm install
	@poetry update

# Clean commands (examples, you can define your own clean-up commands)
clean:
	@echo "Cleaning up..."

clean-npm:
	@rm -rf node_modules

clean-all: clean clean-npm
	@echo "All clean!"

# Run tests.
test:
	@pytest -s -v app/ tests/


# Bump up the version of the application. Usage: `make bump-version VER=minor`.
bump-version:
	@bumpver update --${VER} -n
