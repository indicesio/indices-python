# Changelog

## 0.0.8 (2026-04-18)

Full Changelog: [v0.0.7...v0.0.8](https://github.com/indicesio/indices-python/compare/v0.0.7...v0.0.8)

### Features

* **core:** bump stainless edition for uv ([6e311f3](https://github.com/indicesio/indices-python/commit/6e311f3704dda0053f2ef814244fc154e61f8eef))

## 0.0.7 (2026-04-18)

Full Changelog: [v0.0.6...v0.0.7](https://github.com/indicesio/indices-python/compare/v0.0.6...v0.0.7)

### Features

* **api:** api update ([3ba740c](https://github.com/indicesio/indices-python/commit/3ba740c5cdc505972cddbc2e6b507ca70a51caef))
* **api:** manual updates ([60e1b13](https://github.com/indicesio/indices-python/commit/60e1b13d7eb1a9eca04201b1ff955f426b4bf7b4))


### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([48a9cc7](https://github.com/indicesio/indices-python/commit/48a9cc74c48cf298e4c287e1e08a48aa79789a52))
* ensure file data are only sent as 1 parameter ([979fdd0](https://github.com/indicesio/indices-python/commit/979fdd028c41778f473e041a15dc134913ec5091))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([7b93c78](https://github.com/indicesio/indices-python/commit/7b93c78769f07cc21af555fcb80725d39b4ed2b5))

## 0.0.6 (2026-03-30)

Full Changelog: [v0.0.5...v0.0.6](https://github.com/indicesio/indices-python/compare/v0.0.5...v0.0.6)

### Features

* **api:** api update ([881280f](https://github.com/indicesio/indices-python/commit/881280f7a0984414a0b6edfbf24bc7bdfc1763f3))
* **api:** api update ([31f3044](https://github.com/indicesio/indices-python/commit/31f30445070fcca584ee9633ba1e9a8a943b6093))
* **api:** api update ([ec0d80b](https://github.com/indicesio/indices-python/commit/ec0d80b6b17dcdd4516974c6f733f5a9ddb0666d))
* **api:** api update ([553f602](https://github.com/indicesio/indices-python/commit/553f602cf3205ab95e31d9440b52852d57251d9e))
* **api:** api update ([4909f6a](https://github.com/indicesio/indices-python/commit/4909f6afee52f86e6bd67be2b6a4449c75ca04da))
* **api:** capitalisation ([c3cd371](https://github.com/indicesio/indices-python/commit/c3cd37126d87d619bfea60e746882d88de84724e))
* **internal:** implement indices array format for query and form serialization ([67914c1](https://github.com/indicesio/indices-python/commit/67914c1c39da4a869a153ba278c7cf2eacbc5130))


### Bug Fixes

* **deps:** bump minimum typing-extensions version ([3cb05ab](https://github.com/indicesio/indices-python/commit/3cb05abefb9f78004e9d6f9152538cda80efae4a))
* **pydantic:** do not pass `by_alias` unless set ([a52be24](https://github.com/indicesio/indices-python/commit/a52be245a99de6de7077faf4dfbed7e0002dba08))
* sanitize endpoint path params ([facb6b1](https://github.com/indicesio/indices-python/commit/facb6b128829e92337930fe3259f887c4219a0ac))


### Chores

* **ci:** skip lint on metadata-only changes ([faea39e](https://github.com/indicesio/indices-python/commit/faea39e6ebea556d9803376bcca3026914253307))
* **ci:** skip uploading artifacts on stainless-internal branches ([d2db552](https://github.com/indicesio/indices-python/commit/d2db552f7675fc9017b01d135eec6ee291c64d49))
* **internal:** add request options to SSE classes ([e9a3e79](https://github.com/indicesio/indices-python/commit/e9a3e794aa0309cd57bf7b1d0fa0492e61512247))
* **internal:** codegen related update ([a095bfc](https://github.com/indicesio/indices-python/commit/a095bfc81c8c8c627045072e67c922b6375a115c))
* **internal:** make `test_proxy_environment_variables` more resilient ([66265bf](https://github.com/indicesio/indices-python/commit/66265bfd8973ebb9277316a7f4d8bfda22c06323))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([9a9a342](https://github.com/indicesio/indices-python/commit/9a9a3420d4e45b05aed339581c5c3dcbe199af02))
* **internal:** remove mock server code ([9403e9e](https://github.com/indicesio/indices-python/commit/9403e9ec9b214d8add5087b426bbcb2d1c585f1c))
* **internal:** tweak CI branches ([8f58c2c](https://github.com/indicesio/indices-python/commit/8f58c2c432d856e10668647dd20736b753b45902))
* **internal:** update gitignore ([b7cc4be](https://github.com/indicesio/indices-python/commit/b7cc4be6a776eb2e26107b738ee668176f2b22e4))
* update mock server docs ([ccaed7b](https://github.com/indicesio/indices-python/commit/ccaed7bde4bb2b03062db63204a65621b1372ee4))

## 0.0.5 (2026-02-17)

Full Changelog: [v0.0.4...v0.0.5](https://github.com/indicesio/indices-python/compare/v0.0.4...v0.0.5)

### Features

* **api:** api update ([73e33fb](https://github.com/indicesio/indices-python/commit/73e33fb63037ac7c287b8e6ec422ce67fba82f1d))
* **api:** sync ([6f09f4c](https://github.com/indicesio/indices-python/commit/6f09f4cb006bea86b214d44f5a38c129024427c5))
* **client:** add custom JSON encoder for extended type support ([ff4c567](https://github.com/indicesio/indices-python/commit/ff4c567305a1d0feb329dfd9e59f4a927350e9fd))
* **client:** add support for binary request streaming ([13ebdcc](https://github.com/indicesio/indices-python/commit/13ebdccd3ae8f91647f40d4be3b6a2db378f9ecb))


### Chores

* **ci:** upgrade `actions/github-script` ([88e6850](https://github.com/indicesio/indices-python/commit/88e6850dd2b2ab98b861740813e3de587afeb713))
* format all `api.md` files ([c64b877](https://github.com/indicesio/indices-python/commit/c64b87740a7466d20ee3417c55efd7480e5abc4a))
* **internal:** bump dependencies ([24a923f](https://github.com/indicesio/indices-python/commit/24a923ff97ac88cb84123ba2aa1c57aa7c034a1b))
* **internal:** fix lint error on Python 3.14 ([3ad6e62](https://github.com/indicesio/indices-python/commit/3ad6e624136b8908973b1938d33bbb4dc0906ced))
* **internal:** update `actions/checkout` version ([518badd](https://github.com/indicesio/indices-python/commit/518badde5aadc9c9b2ea75abc61364f9067f18c4))

## 0.0.4 (2026-01-10)

Full Changelog: [v0.0.3...v0.0.4](https://github.com/indicesio/indices-python/compare/v0.0.3...v0.0.4)

### Features

* **api:** add secrets APIs ([16f1cbe](https://github.com/indicesio/indices-python/commit/16f1cbeddd312eb10e1ae813ad40b3ad836dc4e2))
* **api:** add secrets APIs ([19f64f7](https://github.com/indicesio/indices-python/commit/19f64f7d9b9717ad2541c43b86496c39ecbd03cf))

## 0.0.3 (2026-01-10)

Full Changelog: [v0.0.2...v0.0.3](https://github.com/indicesio/indices-python/compare/v0.0.2...v0.0.3)

### Features

* **api:** improve examples ([b2aa0ed](https://github.com/indicesio/indices-python/commit/b2aa0ed184f512b82e245c39b399f32972f68c8f))
* **api:** manual updates ([b7364bb](https://github.com/indicesio/indices-python/commit/b7364bb2260e6fcdb0c7be226087a160320995e3))


### Bug Fixes

* ensure streams are always closed ([69d4b32](https://github.com/indicesio/indices-python/commit/69d4b327e19123f455fca874f2468e798880117c))
* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([57b79b0](https://github.com/indicesio/indices-python/commit/57b79b0bf617bee7bb445bd53aa34183325296ce))
* use async_to_httpx_files in patch method ([126eb61](https://github.com/indicesio/indices-python/commit/126eb613c202fdddf23808aacbdbdf675bcdccd2))


### Chores

* add missing docstrings ([8df9ee8](https://github.com/indicesio/indices-python/commit/8df9ee89d5143935931215e42602695ec1ea065c))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([e64b0a1](https://github.com/indicesio/indices-python/commit/e64b0a1fc2c5e067516938b2df54f1bda4523b0c))
* **docs:** use environment variables for authentication in code snippets ([9c03911](https://github.com/indicesio/indices-python/commit/9c0391185cfe2a091e2309dad60ce49dc447f394))
* **internal:** add `--fix` argument to lint script ([d783aed](https://github.com/indicesio/indices-python/commit/d783aedc00622a00a9ad0c93caed2c57db1e68ff))
* **internal:** add missing files argument to base client ([0493ee7](https://github.com/indicesio/indices-python/commit/0493ee7da82202ba3b442bef83b787d4a0137e38))
* **internal:** codegen related update ([b7f5b02](https://github.com/indicesio/indices-python/commit/b7f5b025e6443645688cebd3ecb9de0493e45f61))
* speedup initial import ([02a4942](https://github.com/indicesio/indices-python/commit/02a4942f1dea08583414c4d2a25507d6db3d406d))
* update lockfile ([12e35b4](https://github.com/indicesio/indices-python/commit/12e35b4b0170fb54100b1c1d98006317592b3fb3))

## 0.0.2 (2025-11-27)

Full Changelog: [v0.0.1...v0.0.2](https://github.com/indicesio/indices-python/compare/v0.0.1...v0.0.2)

### Features

* **api:** config updates ([88eadb3](https://github.com/indicesio/indices-python/commit/88eadb3d17bb0ada31c4fcd6fed1838d47916e81))
* **api:** update openapi spec (v1beta, etc) ([546f449](https://github.com/indicesio/indices-python/commit/546f44918e9b02c6cda3abcab760f2d954e955ec))


### Bug Fixes

* **client:** close streams without requiring full consumption ([959e13b](https://github.com/indicesio/indices-python/commit/959e13b69b92580d77aaa31f33adc3abccb50589))
* compat with Python 3.14 ([a37a195](https://github.com/indicesio/indices-python/commit/a37a1954165cc58e4b2f48cf8fb071455b191900))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([b4d1653](https://github.com/indicesio/indices-python/commit/b4d165320434b8447770e0cb417be404d21e0559))


### Chores

* add Python 3.14 classifier and testing ([541071b](https://github.com/indicesio/indices-python/commit/541071bf220a04ad50593691d34f2d3a96848f5f))
* **internal/tests:** avoid race condition with implicit client cleanup ([844f1fb](https://github.com/indicesio/indices-python/commit/844f1fb36c363c4e60d05bd311ed96115db3244c))
* **internal:** grammar fix (it's -&gt; its) ([49e8427](https://github.com/indicesio/indices-python/commit/49e8427b5299817d6bc5a06cec3deed1f164cbc0))
* **package:** drop Python 3.8 support ([daf5eee](https://github.com/indicesio/indices-python/commit/daf5eee6e9478719c680e775530b436b90870a84))

## 0.0.1 (2025-10-20)

Full Changelog: [v0.0.1...v0.0.1](https://github.com/indicesio/indices-python/compare/v0.0.1...v0.0.1)

### Features

* **api:** manual updates ([bd1ba01](https://github.com/indicesio/indices-python/commit/bd1ba01702edb85b98309a8f4b8b626c7a4f34f1))


### Chores

* update SDK settings ([29395f4](https://github.com/indicesio/indices-python/commit/29395f42da941577e78d2e18f310dfdfac11e044))
* update SDK settings ([7e79028](https://github.com/indicesio/indices-python/commit/7e79028fed7be3b520ff233352d28d0b9518d2ab))
