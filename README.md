# SAS Customer Intelligence 360 — API Plan Library

## Overview

The Plan API for SAS Customer Intelligence 360 provides resources for accessing the planning capabilities of SAS 360 Plan. The API enables you to access planner resources to manage planning instances and integrate them with enterprise systems. For example, you could use the API to create and manage instances of planner resources as a response to events that are external to SAS 360 Plan.

For detailed information on the REST API:<br>
https://support.sas.com/documentation/onlinedoc/ci/ci360-apis/marketingPlan/v2/redoc.html
<br><br>

### Table of Contents

This topic contains the following sections:

 - <a href="#prerequisites">Prerequisites</a>
 - <a href="#installation">Installation</a>
 - <a href="#getting-started">Getting Started</a>
 - <a href="#api-plan-code">API Plan Code</a>
 - <a href="#branches">Branches</a>
 - <a href="#contributing">Contributing</a>
 - <a href="#license">License</a>
 - <a href="#additional-resources">Additional Resources</a>
<br><br>

### Prerequisites

 * Required Python: >=3.6
 * Customer Intelligence 360 Tenant with Administrative Rights
 * The `sasci360apicore` library, which provides the shared connection and JWT-signing logic this package builds on
<br><br>

### Installation

This library isn't published to a public package index. To install it from source:

 1. Clone this repository and `cd` into it
 2. Install the runtime dependencies:<br>
    `pip install -r requirements.txt`
 3. Install the package itself:<br>
    `pip install .` (or `pip install -e .` for an editable/development install)
<br><br>

### Getting Started

While this library is available for review, please note that it is considered a work in process and NOT considered "released for production".
<br><br>

### API Plan Code

 1. Budget Hierarchy - Contains the operations for a planning hierarchy's budget details.
 1. Business Units - Contains the operations for business unit collections.
 1. Commitments - Contains the operations for commitment collections.
 1. Cost Centers - Contains the operations for cost center collections.
 1. Financial Accounts - Updates the specified financial account based on the representation in the request body.
 1. Hierarchy Definitions - Contains the operations for business unit collections.
 1. Hierarchy Definition Levels - Contains the operations for a hierarchy level resource.
 1. Invoices - Contains the operations for invoice collections.
 1. Planning Items - Contains the operations for planning item collections.
 1. Root - Contains the operations for the root resource.
 1. Settings - Returns the representation of the specified setting.
 1. Vendors - Contains the operations for a vendor resource.
<br><br>

### Branches

 - `main` — stable, released code
 - `staging` — pre-release testing
 - `develop` — active integration branch for ongoing work
<br><br>

### Contributing

We welcome your contributions! Please read [CONTRIBUTING](CONTRIBUTING.md) for details on how to submit contributions to this project.
<br><br>

### License

This project is licensed under the [Nelson Grey LLC Community License 1.0](LICENSE).

- **Free for individuals, education, and research**: use, modify, and distribute this software for non-commercial purposes
- **Commercial evaluation**: evaluate the software for a possible commercial use, free of charge
- **Commercial production use**: requires a commercial license from Nelson Grey LLC
- **Automatic conversion**: on December 13, 2029, this automatically converts to the Apache License 2.0

For commercial licensing inquiries, contact support@nelsongrey.com.

### Additional Resources

For more information, see [REST APIs](https://go.documentation.sas.com/doc/en/cintcdc/production.a/cintapis/ch-rest-apis.htm).
<br><br>
