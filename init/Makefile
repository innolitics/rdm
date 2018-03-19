.SUFFIXES:

RELEASE_DIR := release

$(RELEASE_DIR)/development_plan.md: templates/base.md templates/development_plan.md data/system.yml data/requirements.yml
	@mkdir -p $(@D)
	rdm templates/development_plan.md data/system.yml data/requirements.yml > $@
