# Floridayvine CLI Documentation

## Main Command

```shell
                                                                                                                                                   
 Usage: floridayvine [OPTIONS] COMMAND [ARGS]...                                                                                                   
                                                                                                                                                   
╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                                                                         │
│ --show-completion             Show completion for the current shell, to copy it or customize the installation.                                  │
│ --help                        Show this message and exit.                                                                                       │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ about       Display information about the Floriday Vine command line interface.                                                                 │
│ db          Database management commands.                                                                                                       │
│ inventory   Inventory management commands.                                                                                                      │
│ sync        Synchronize collections in the local database with Floriday.                                                                        │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```

## `about` Command

```
                                                                                                                                                   
 Usage: floridayvine about [OPTIONS] COMMAND [ARGS]...                                                                                             
                                                                                                                                                   
 Display information about the Floriday Vine command line interface.                                                                               
                                                                                                                                                   
╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                                                                     │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ show-info   Display information about Floriday Vine, its connection to Floriday, and database status.                                           │
│ version     Display the current version of Floriday Vine.                                                                                       │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```

## `db` Command

```
                                                                                                                                                   
 Usage: floridayvine db [OPTIONS] COMMAND [ARGS]...                                                                                                
                                                                                                                                                   
 Database management commands.                                                                                                                     
                                                                                                                                                   
╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                                                                     │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ init                                                                                                                                            │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```

## `inventory` Command

```
                                                                                                                                                   
 Usage: floridayvine inventory [OPTIONS] COMMAND [ARGS]...                                                                                         
                                                                                                                                                   
 Inventory management commands.                                                                                                                    
                                                                                                                                                   
╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                                                                     │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ list-direct-sales   List all direct sales from Floriday.                                                                                        │
│ list-trade-items    List all trade items from Floriday.                                                                                         │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```

## `sync` Command

```
                                                                                                                                                   
 Usage: floridayvine sync [OPTIONS] COMMAND [ARGS]...                                                                                              
                                                                                                                                                   
 Synchronize collections in the local database with Floriday.                                                                                      
                                                                                                                                                   
╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                                                                     │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ organizations   Synchronize organizations data from Floriday.                                                                                   │
│ status          Display the synchronization status for all synchronized collections.                                                            │
│ supply-lines    Synchronize supply lines data from Floriday.                                                                                    │
│ trade-items     Synchronize trade items data from Floriday.                                                                                     │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```

