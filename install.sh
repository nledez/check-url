#!/usr/bin/env bash

if [ ! -d .venv ]; then
	python3 -m venv .venv
fi

NEED_PIP_INSTALL=

./.venv/bin/pip freeze > .pip.freeze

while IFS= read -r p; do
	echo "Check ${p} package"
	grep "${p}" .pip.freeze || NEED_PIP_INSTALL=yes
	if [ -n "${NEED_PIP_INSTALL}" ]; then
		echo "Need install"
		./.venv/bin/pip install -r requirements.txt
		break
	fi
done < requirements.txt
