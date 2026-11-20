# Sergipe Surf Federation: web platform

[← Back to profile](../README.md) · [🇧🇷 Português](./pt-br/fss.md)

| | |
| --- | --- |
| **Client** | Federação Sergipana de Surf (state surfing federation, Brazil) |
| **Role** | Developer: web application, back-end integration and releases |
| **Status** | In development (private repository) |

## Context

A state sports federation needed a digital presence and administrative tools to manage its operations, which had previously been handled manually.

## Scope

- Public website and authenticated areas
- Administrative workflows for the federation's team
- Integration between the web application and the back-end
- Role-based permissions for different user profiles

## Engineering practices

- **Separate environments:** staging and production are isolated, and changes are validated before release.
- **Access control:** permissions are defined per role, following least privilege.
- **Gradual rollout:** features are released step by step, with configuration reviewed at each stage.
- **Data protection:** institutional and member data is never exposed in public material.
