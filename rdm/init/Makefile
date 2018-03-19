.SUFFIXES:

RELEASE_DIR := release

$(RELEASE_DIR)/development_plan.md: templates/development_plan.md data/system.yml data/requirements.yml
	@mkdir -p $(@D)
	rdm render templates/development_plan.md data/system.yml data/requirements.yml > $@
