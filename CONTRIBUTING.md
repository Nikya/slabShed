# How to contribute

Fallow this instructions to produce your own *Slab Shed* collection.

## TODO check list

- [ ] **Duplicate** the folder content `./collections/_SlabShed_duplicateMe`
- [ ] With a _conventioned name_
    - [ ] **Rename** the duplicated folder
    - [ ] Change the top-**title** of this `README`
- [ ] Write an **introduction** of your collection in the `README` section _§description_.
- [ ] Take one or more **overview _photo_** or _screenshot_ of your collection.
    - Put in the root folder of this collection with _conventioned name_ 
    - Adapt the README section _§Overview_
- [ ] Put in `source` folder, all **files used to build** this collection (.FCStd, .blend, ...) with _conventioned name_.
- [ ] Put in `distributable` folder, all **final files** that can be used directly for 3D printing (.stl, .obj, ...)
- [ ] For each Slab and Shed
    - Take a screenshot 
    - Put in the _root folder_ of this collection with _conventioned name_
    - Adapt the `README` section
        - _§Slab_: With pictures and short description
        - _§Shed_: With pictures and short description and composition
- Share your work!
    - From the initial project https://github.com/Nikya/slabShed
        - You can offer a _push request_
        - Or a message to be integrated into the COLLECTION page

## Naming convention

### Collection Name

- For **Slab and Shed** collection
    - Title: `Slab and Shed - My Collection Name collection`
    - Folder: `slabShed_MyCollectionName`
- For **slab only** collection 
    - Title: `Slab - My Collection Name collection`
    - Folder: `slab_MyCollectionName`
- For **shed only** collection 
    - Title: `Shed - My Collection Name collection`
    - Folder: `shed_MyCollectionName`

### Overview picture name

Juste like `overview999.png` where 999 start at 1 for the **first mandatory overview picture**.

### Slab name

Like `slab_MyCollectionName_SlabName`, where 
- **MyCollectionName** : Is the name of the current collection
- **SlabName** : Is the name of the current slab

To be used for **slab** picture, **source** file, **distributable** file.

### Shed name

Like `shed_99_88x77_MyCollectionName_ShedName`, where 
- **99** : Is the real total rack capacity of the shed
- **88** : Is the maximum rack width capacity of the shed
- **77** : Is the maximum rack hight capacity of the shed
- **MyCollectionName** : Is the name of the current collection
- **ShedName** : Is the name of the current shed

### Images 

Recomanded (not mandatory) images size for overview and picture :
- ratio 4:3 as 480x360px
- ratio 1:1 as 360x360px

## Technical and Artistic constraints

### Base

The **_base_** part of a _Slab_ must be design like this:

- Width: 20cm
- Hight: 20cm
- Depth: 5cm
- Corner radius: 4,5cm
- Must keep a _foolproof insert_ in the bottom right corner.

### Sculp

The **artistic** part of a _Slab_ is more free, it just must not destabilize the balance or weaken the _slab_ too much. It can be:

- an high-relief (sculpture)
- an bas-relief 
- an engraving (-1mm)
- an protrusion (+1mm)
- ...