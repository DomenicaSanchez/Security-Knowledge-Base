# Topics
- [[#Regular expressions]]
- [[#Permission Management]]
___
## Regular expressions

Regular expressions (RE) are sequences of characters or simbols that together form a search pattern.
These patterns often include special symbols called **metacharacters**, which define the structure of the search.

### Grouping Operation
![[Pasted image 20251019120432.png]]

| Operation | define                                                  |
| --------- | ------------------------------------------------------- |
| `(a)`     | Groups characters as a single unit                      |
| `[a-z]`   | Matches any letter from a to z                          |
| \|        | Means "or"  - matches one expression or another         |
| .*        | Means "and" -  matches  one expression and other        |
| \b        | Matches expressions that begin with a pattern           |
| $         | Matches expressions that end with the specified pattern |

## Permission Management


![[Permission Managment.png]]
### Change permissions
We can modify permissions using `chmod` . You can add (`+`) or remove (`-`) permission group reference:

| Group  | Option |
| ------ | ------ |
| owner  | `u`    |
| Group  | `g`    |
| others | `o`    |
| All    | `a`    |
Example
![[Changed Permissions.png]]
## Change owner
We can modify ownership using `chown`. This command doesn’t change permissions - it changes who owns the file or folder. 
![[Change owner.png]]

## Sticky Bit
The sticky bit locks files in a shared directory so that only the file owner, directory owner, or root can delete or rename them.  
`t` means others have execute permission, `T` means they do not.
![[Sticky Bit.png]]
___
- **Previous** : [[Introduction to Shell]]
___

