.PHONY: build

build:
	sam build

deploy-infra:
	sam build && aws-vault exec crc --no-session -- sam deploy --no-confirm-changeset

deploy-site:
	aws-vault exec crc --no-session -- aws s3 sync ./resume-site s3://this-isnt-gonna-wrk650269

invoke-get:
	sam build && aws-vault exec crc --no-session -- sam local invoke GetFunction

invoke-put:
	sam build && aws-vault exec crc --no-session -- sam local invoke PutFunction
