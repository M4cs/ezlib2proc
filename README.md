# ezlib2proc
Python TUI tool to wrap lib2proc and make loading/unloading libraries easier | Support for Mono

# Usage

**Requirements:**

- [lib2proc (From UnKnoWnCheaTs)](https://www.unknowncheats.me/forum/pc-software/214802-lib2proc-definitive-os-macos-injector.html)
- Python 3

`sudo python3 ezlib2proc.py`

# Documentation

Somewhere in your loader class you should include both a loading and unloading function. In the example class below you can see the loader method called `Init` and the unloading method called `Unload`:

```csharp
using UnityEngine;

namespace UnityCheat
{
    public class MyLoader
    {
        static void Init()
        {
            UnityCheat.Load = new GameObject();
            UnityCheat.Load.AddComponent<THEHACKCLASS>();
            UnityEngine.Object.DontDestroyOnLoad(UnityCheat.Load);
        }

        static void Unload()
        {
            GameObject.Destroy(UnityCheat.Load);
        }

        private static GameObject Load;
    }
}
```

You will pass `Init` as the Loader Method in `ezlib2proc` and `Unload` as the Unload Method.
