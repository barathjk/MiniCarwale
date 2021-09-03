# TEST PLAN

## Table no: High Level Test Plan

| **Test ID** | **Description**                   | **Exp I/P** | **Exp O/P** | **Actual O/P** |    
|-------------|-----------------------------------|------------|-------------|----------------|
|  H_01       | EMI Calculations | Choice | SUCCESS | SUCCESS |


## Table no: Low Level Test Plan

| **Test ID** | **HL_ID** | **Description**   | **Exp Input** | **Exp Output** | **Actual Output** |**Type Of Test**  |    
|-------------|-----------|---------------------------|------------|-------------|----------------|------------------|
|  L_01      | H_01 | Performing EMI calculations for altrozpositive  | (800000, 9.25, 5) | 16703.92 | 16703.92 | Requirement based |
|  L_02       | H_01 | Performing EMI calculations for city | (-800000, 9, 5) | None | None | Requirement based |
|  L_03      | H_01 | Performing EMI calculations for altroznull | (0, 0.021, -5) | None | None | Requirement based |
|  L_04       | H_01 | Performing EMI calculations for i20  | (500000, 12.5, 3) | 16726.81 | 16726.81 | Requirement based |
|  L_05       | H_01 | Performing EMI calculations for harriernegative | (-800000, 9, 5) | None | None | Requirement based |
|  L_06       | H_01 | Performing EMI calculations for harriernull | (0, 0.021, -5) | None | None | Requirement based |
|  L_07       | H_01 | Performing EMI calculations for ciaz  | (800000, 9.25, 5) | 16703.92 | 16703.92 | Requirement based |
|  L_08       | H_01 | Performing EMI calculations for nexonnegative | (-800000, 9, 5) | None | None | Requirement based |
|  L_09       | H_01 | Performing EMI calculations for nexonnull | (0, 0.021, -5) | None | None | Requirement based |
|  L_10      | H_01 | Performing EMI calculations for swiftpositive  | (600000, 6.5, 2) | 26727.75 | 26727.75 | Requirement based |
|  L_11       | H_01 | Performing EMI calculations for swiftnegative | (-800000, 9, 5) | None | None | Requirement based |
|  L_12       | H_01 | Performing EMI calculations for swiftnull | (0, 0.021, -5) | None | None | Requirement based |
|  L_13       | H_01 | Performing EMI calculations for jazz  | (425000, 8.5, 5) | 8719.53 | 8719.53 | Requirement based |
|  L_14       | H_01 | Performing EMI calculations for vitaranegative | (-800000, 9, 5) | None | None | Requirement based |
|  L_15       | H_01 | Performing EMI calculations for vitaranull | (0, 0.021, -5) | None | None | Requirement based |
|  L_16       | H_01 | Performing EMI calculations for ciazpositive  | (800000, 9.25, 5) | 16703.92 | 16703.92 | Requirement based |
|  L_17       | H_01 | Performing EMI calculations for wrv | (200000, 6.75, 4) | 4766.09  | 4766.09  | Requirement based |
|  L_18       | H_01 | Performing EMI calculations for ciaznull | (0, 0.021, -5) | None | None | Requirement based |
|  L_19      | H_01 | Performing EMI calculations for ciazpositive  | (800000, 9.25, 5) | 16703.92 | 16703.92 | Requirement based |
|  L_20       | H_01 | Performing EMI calculations for rapid | (-800000, 9, 5) | None | None | Requirement based |
|  L_21       | H_01 | Performing EMI calculations for superb | (0, 0.021, -5) | None | None | Requirement based |
|  L_22       | H_01 | Performing EMI calculations for city  | (800000, 9.25, 5) | 16703.92 | 16703.92 | Requirement based |
|  L_23       | H_01 | Performing EMI calculations for octavia | (3000000, 9.25, 5) | 62639.69  | 62639.69  | Requirement based |
|  L_24       | H_01 | Performing EMI calculations for verna | (0, 0.021, -5) | None | None | Requirement based |
