# Write your code here
"""# Assignment

Translate this function `includes(xs, ys)` that checks if all elements of `ys` also appear in `xs`.

```javascript
function includes(xs, ys)
{
    for ( const y of ys )
    {
        // Look for a way to check for list membership in Python
        if ( !xs.includes(y) )
        {
            return false;
        }
    }

    return true;
}
"""
def includes(xs, ys):
    for y in ys:
        if y not in xs:
            return False
    return True
