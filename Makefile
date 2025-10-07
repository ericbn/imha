.PHONY: venv git-hooks test

VENVDIR := .venv

$(VENVDIR): .python-version
	@uv venv --clear --seed

venv: | $(VENVDIR)
	@uv sync

.git/hooks/%: $(VENVDIR)/bin/pre-commit | venv
	@$(VENVDIR)/bin/pre-commit install --hook-type $(@F)

git-hooks: .git/hooks/pre-commit

test: $(VENVDIR)/bin/pytest | venv
	@$(VENVDIR)/bin/pytest -vv
