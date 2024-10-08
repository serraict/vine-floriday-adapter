# Floridayvine CLI Documentation

## Main Command

```shell
                                                                                                                                                        
 Usage: floridayvine [OPTIONS] COMMAND [ARGS]...                                                                                                        
                                                                                                                                                        
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                                                                              │
│ --show-completion             Show completion for the current shell, to copy it or customize the installation.                                       │
│ --help                        Show this message and exit.                                                                                            │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ db                                                                                                                                                   │
│ floriday                                                                                                                                             │
│ sync                                                                                                                                                 │
│ version                                                                                                                                              │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```

## `db` Command

```
                                                                                                                                                        
 Usage: floridayvine db [OPTIONS] COMMAND [ARGS]...                                                                                                     
                                                                                                                                                        
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                                                                          │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ init                                                                                                                                                 │
│ print-sync-status                                                                                                                                    │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```

## `floriday` Command

```
                                                                                                                                                        
 Usage: floridayvine floriday [OPTIONS] COMMAND [ARGS]...                                                                                               
                                                                                                                                                        
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                                                                          │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ floriday-connection-info                                                                                                                             │
│ print-direct-sales                                                                                                                                   │
│ print-trade-items                                                                                                                                    │
│ sync                                                                                                                                                 │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```

## `sync` Command

```
                                                                                                                                                        
 Usage: floridayvine sync [OPTIONS] COMMAND [ARGS]...                                                                                                   
                                                                                                                                                        
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                                                                          │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ organizations   Synchronize organizations data from Floriday.                                                                                        │
│ trade-items     Synchronize trade items data from Floriday.                                                                                          │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```

## `version` Command

```
                                                                                                                                                        
 Usage: floridayvine version [OPTIONS] COMMAND [ARGS]...                                                                                                
                                                                                                                                                        
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                                                                          │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ about                                                                                                                                                │
│ print-version                                                                                                                                        │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```

