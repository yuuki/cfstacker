REGION=ap-northeast-1
STACKER=bin/cfstacker # Just use 'cfstacker' on your environment

.PHONY: s3/prod/create
s3/prod/create:
	$(STACKER) create s3 -e prod

.PHONY: s3/prod/update
s3/prod/update:
	$(STACKER) update s3 -e prod

.PHONY: s3/prod/validate
s3/prod/validate:
	$(STACKER) validate s3 -e prod

# ---------------------------------

.PHONY: iam/staging/create
iam/staging/create:
	$(STACKER) create iam -e staging

.PHONY: iam/staging/update
iam/staging/update:
	$(STACKER) update iam -e staging

.PHONY: iam/staging/validate
iam/staging/validate:
	$(STACKER) validate iam -e staging

# ---------------------------------

.PHONY: iam/prod/create
iam/prod/create:
	$(STACKER) create iam -e prod

.PHONY: iam/prod/update
iam/prod/update:
	$(STACKER) update iam -e prod

.PHONY: iam/prod/validate
iam/prod/validate:
	$(STACKER) validate iam -e prod
