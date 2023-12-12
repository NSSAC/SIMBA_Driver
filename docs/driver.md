# SIMBA Driver

- [1. [Optional] Property SIMBA Driver > runId](#runId)
- [2. [Optional] Property SIMBA Driver > cellId](#cellId)
- [3. [Optional] Property SIMBA Driver > initialTick](#initialTick)
- [4. [Required] Property SIMBA Driver > initialTime](#initialTime)
- [5. [Required] Property SIMBA Driver > endTime](#endTime)
- [6. [Optional] Property SIMBA Driver > continueFromTick](#continueFromTick)
- [7. [Required] Property SIMBA Driver > scheduleIntervals](#scheduleIntervals)

**Title:** SIMBA Driver

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

**Description:** The schema describes how the SIMBA driver is executed

<details>
<summary><strong> <a name="runId"></a>1. [Optional] Property SIMBA Driver > runId</strong>  

</summary>
<blockquote>

**Title:** A unique ID identifying the run to be executed

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
</details>

<details>
<summary><strong> <a name="cellId"></a>2. [Optional] Property SIMBA Driver > cellId</strong>  

</summary>
<blockquote>

**Title:** A unique ID identifying the currently running experimental setup

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
</details>

<details>
<summary><strong> <a name="initialTick"></a>3. [Optional] Property SIMBA Driver > initialTick</strong>  

</summary>
<blockquote>

**Title:** The initial Tick

| Type                      | `integer`                                                                 |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
</details>

<details>
<summary><strong> <a name="initialTime"></a>4. [Required] Property SIMBA Driver > initialTime</strong>  

</summary>
<blockquote>

**Title:** Time associated with the initial tick

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

</blockquote>
</details>

<details>
<summary><strong> <a name="endTime"></a>5. [Required] Property SIMBA Driver > endTime</strong>  

</summary>
<blockquote>

**Title:** The stooping time of the simulation

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

**Description:** The simulation stops once initialTime plus all accumulated durations (timePerTick) exceeds the endTime

</blockquote>
</details>

<details>
<summary><strong> <a name="continueFromTick"></a>6. [Optional] Property SIMBA Driver > continueFromTick</strong>  

</summary>
<blockquote>

**Title:** Optional Continuation

| Type                      | `integer`                                                                 |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `"initialTick"`                                                           |
|                           |                                                                           |

**Description:** This attribute allows to continue a previously executed simulation at the given tick

</blockquote>
</details>

<details>
<summary><strong> <a name="scheduleIntervals"></a>7. [Required] Property SIMBA Driver > scheduleIntervals</strong>  

</summary>
<blockquote>

**Title:** Scheduled Simulation Intervals

| Type                      | `array of object`                                                         |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

**Description:** The intervals are executed in the listed order and must not overlap.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |
|                      |                    |

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2023-12-12 at 11:44:54 -0500