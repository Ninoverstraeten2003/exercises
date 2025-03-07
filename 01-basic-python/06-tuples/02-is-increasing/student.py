# Write your code here
"""# Assignment

Translate the function below:

```javascript
function isIncreasing(ns)
{
    // Rely on zip
    for ( let i = 0; i + 1 < ns.length; ++i )
    {
        const x = ns[i];
        const y = ns[i + 1];

        if ( x > y )
        {
            return false;
        }
    }

    return true;
}
```
"""
def is_increasing(ns):
    for (x, y) in zip(ns,ns[1:]):
        if x > y:
            return False
    return True
