# Playwright CLI Workflows

## Basic page walkthrough

```bash
"$PWCLI" open https://example.com
"$PWCLI" snapshot
"$PWCLI" click e3
"$PWCLI" snapshot
```

## Form fill

```bash
"$PWCLI" open https://example.com/form
"$PWCLI" snapshot
"$PWCLI" fill e1 "user@example.com"
"$PWCLI" fill e2 "password123"
"$PWCLI" click e3
"$PWCLI" snapshot
```

## Visual debugging

```bash
"$PWCLI" open https://example.com --headed
"$PWCLI" snapshot
"$PWCLI" screenshot
```

When refs stop working, re-run `snapshot` before trying the next interaction.
