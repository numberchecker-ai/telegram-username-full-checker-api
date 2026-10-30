# Telegram Username Full Checker API — retired

> [!IMPORTANT]
> The former `tg_username_full` product (ID 81) is retired. New tasks are rejected. The example entry points in this repository stop locally and do not submit a request.

This repository is retained as historical integration context. It does not advertise a currently available Full Checker product, and its former product URL is no longer a valid landing page.

## Choose a supported product deliberately

The current Telegram username pipeline has separate registration, activity and profile stages. Its product catalog includes `tg_username` (78), `tg_username_activity` (79) and `tg_username_profile` (80), but not `tg_username_full` (81). These are not interchangeable response contracts; do not just rename an old task type and assume the same fields, limits or price.

- [Current Username Checker examples](https://github.com/numberchecker-ai/telegram-username-checker-api)
- [Current Username Profile examples](https://github.com/numberchecker-ai/telegram-username-profile-checker-api)
- [Current Username Profile product](https://numberchecker.ai/products/telegram-username-profile-checker)
- [Account and current available products](https://platform.numberchecker.ai)

Use the current product’s README and result fields before migrating. Existing historical task IDs may still be queried through the normal task-status API; this repository does not change stored tasks or automatically migrate them.

The sample code remains [MIT licensed](LICENSE). [openapi.yaml](openapi.yaml) intentionally contains no active operations for this retired product.

*Last reviewed: 2026-10-30 · Maintained by NumberChecker.*
