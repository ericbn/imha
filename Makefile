.PHONY: venv git-hooks test

VENVDIR := .venv

$(VENVDIR): .python-version
	@uv venv --clear --seed

venv: | $(VENVDIR)
	@uv sync

git-hooks:
	@prek install

test: $(VENVDIR)/bin/pytest | venv
	@$(VENVDIR)/bin/pytest -vv
