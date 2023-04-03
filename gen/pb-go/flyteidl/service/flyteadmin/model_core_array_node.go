/*
 * flyteidl/service/admin.proto
 *
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * API version: version not set
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */

package flyteadmin

type CoreArrayNode struct {
	Node *CoreNode `json:"node,omitempty"`
	// Defines the minimum number of instances to bring up concurrently at any given point. Note that this is an optimistic restriction and that, due to network partitioning or other failures, the actual number of currently running instances might be more. This has to be a positive number if assigned. Default value is size.
	Parallelism string `json:"parallelism,omitempty"`
	// An absolute number of the minimum number of successful completions of subtasks. As soon as this criteria is met, the array job will be marked as successful and outputs will be computed. This has to be a non-negative number if assigned. Default value is size (if specified).
	MinSuccesses string `json:"min_successes,omitempty"`
	// If the array job size is not known beforehand, the min_success_ratio can instead be used to determine when an array job can be marked successful.
	MinSuccessRatio float32 `json:"min_success_ratio,omitempty"`
}
