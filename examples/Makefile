REGION=ap-northeast-1
STACKER=bin/stacker # Just use 'stacker' on your environment

.PHONY: s3/prod/create
s3/prod/create:
	$(STACKER) create s3 -e prod

.PHONY: s3/prod/update
s3/prod/update:
	$(STACKER) update s3 -e prod

.PHONY: s3/prod/validate
s3/prod/validate:
	$(STACKER) validate s3 -e prod
