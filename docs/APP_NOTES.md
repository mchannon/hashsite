# Hashsite App Notes

## Modes

Recommended state machine:

```text
edit
read
preview
path-edit
```

Cold open defaults to `edit`. Opening a received Hashsite or Hashpath defaults to `read`. Tapping preview enters `preview`, which is reader mode with a clear return-to-edit control.

## Share object priority

When previewing:

```text
if hashpath exists:
  preview hashpath reader
else if red exists:
  preview red as one-step path
else if green exists:
  preview green as one-step path
else if blue exists:
  preview blue as one-step path
else:
  disable preview
```

## URL split

Public compact links should remain simple.

```text
https://hashsite.org#7B66A3MM2
https://hashsite.org?m=read&p=<hashpath>
```

Hashpath grammar/spec links should point to `hashpath.org`.
