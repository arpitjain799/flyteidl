// Code generated by protoc-gen-validate. DO NOT EDIT.
// source: flyteidl/plugins/sagemaker/training_job.proto

package plugins

import (
	"bytes"
	"errors"
	"fmt"
	"net"
	"net/mail"
	"net/url"
	"regexp"
	"strings"
	"time"
	"unicode/utf8"

	"github.com/golang/protobuf/ptypes"
)

// ensure the imports are used
var (
	_ = bytes.MinRead
	_ = errors.New("")
	_ = fmt.Print
	_ = utf8.UTFMax
	_ = (*regexp.Regexp)(nil)
	_ = (*strings.Reader)(nil)
	_ = net.IPv4len
	_ = time.Duration(0)
	_ = (*url.URL)(nil)
	_ = (*mail.Address)(nil)
	_ = ptypes.DynamicAny{}
)

// define the regex for a UUID once up-front
var _training_job_uuidPattern = regexp.MustCompile("^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$")

// Validate checks the field values on InputMode with the rules defined in the
// proto definition for this message. If any rules are violated, an error is returned.
func (m *InputMode) Validate() error {
	if m == nil {
		return nil
	}

	return nil
}

// InputModeValidationError is the validation error returned by
// InputMode.Validate if the designated constraints aren't met.
type InputModeValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e InputModeValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e InputModeValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e InputModeValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e InputModeValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e InputModeValidationError) ErrorName() string { return "InputModeValidationError" }

// Error satisfies the builtin error interface
func (e InputModeValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sInputMode.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = InputModeValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = InputModeValidationError{}

// Validate checks the field values on AlgorithmName with the rules defined in
// the proto definition for this message. If any rules are violated, an error
// is returned.
func (m *AlgorithmName) Validate() error {
	if m == nil {
		return nil
	}

	return nil
}

// AlgorithmNameValidationError is the validation error returned by
// AlgorithmName.Validate if the designated constraints aren't met.
type AlgorithmNameValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e AlgorithmNameValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e AlgorithmNameValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e AlgorithmNameValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e AlgorithmNameValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e AlgorithmNameValidationError) ErrorName() string { return "AlgorithmNameValidationError" }

// Error satisfies the builtin error interface
func (e AlgorithmNameValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sAlgorithmName.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = AlgorithmNameValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = AlgorithmNameValidationError{}

// Validate checks the field values on MetricDefinition with the rules defined
// in the proto definition for this message. If any rules are violated, an
// error is returned.
func (m *MetricDefinition) Validate() error {
	if m == nil {
		return nil
	}

	// no validation rules for Name

	// no validation rules for Regex

	return nil
}

// MetricDefinitionValidationError is the validation error returned by
// MetricDefinition.Validate if the designated constraints aren't met.
type MetricDefinitionValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e MetricDefinitionValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e MetricDefinitionValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e MetricDefinitionValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e MetricDefinitionValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e MetricDefinitionValidationError) ErrorName() string { return "MetricDefinitionValidationError" }

// Error satisfies the builtin error interface
func (e MetricDefinitionValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sMetricDefinition.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = MetricDefinitionValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = MetricDefinitionValidationError{}

// Validate checks the field values on AlgorithmSpecification with the rules
// defined in the proto definition for this message. If any rules are
// violated, an error is returned.
func (m *AlgorithmSpecification) Validate() error {
	if m == nil {
		return nil
	}

	// no validation rules for InputMode

	// no validation rules for AlgorithmName

	// no validation rules for AlgorithmVersion

	for idx, item := range m.GetMetricDefinitions() {
		_, _ = idx, item

		if v, ok := interface{}(item).(interface{ Validate() error }); ok {
			if err := v.Validate(); err != nil {
				return AlgorithmSpecificationValidationError{
					field:  fmt.Sprintf("MetricDefinitions[%v]", idx),
					reason: "embedded message failed validation",
					cause:  err,
				}
			}
		}

	}

	return nil
}

// AlgorithmSpecificationValidationError is the validation error returned by
// AlgorithmSpecification.Validate if the designated constraints aren't met.
type AlgorithmSpecificationValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e AlgorithmSpecificationValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e AlgorithmSpecificationValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e AlgorithmSpecificationValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e AlgorithmSpecificationValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e AlgorithmSpecificationValidationError) ErrorName() string {
	return "AlgorithmSpecificationValidationError"
}

// Error satisfies the builtin error interface
func (e AlgorithmSpecificationValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sAlgorithmSpecification.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = AlgorithmSpecificationValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = AlgorithmSpecificationValidationError{}

// Validate checks the field values on TrainingJobResourceConfig with the rules
// defined in the proto definition for this message. If any rules are
// violated, an error is returned.
func (m *TrainingJobResourceConfig) Validate() error {
	if m == nil {
		return nil
	}

	// no validation rules for InstanceCount

	// no validation rules for InstanceType

	// no validation rules for VolumeSizeInGb

	return nil
}

// TrainingJobResourceConfigValidationError is the validation error returned by
// TrainingJobResourceConfig.Validate if the designated constraints aren't met.
type TrainingJobResourceConfigValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e TrainingJobResourceConfigValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e TrainingJobResourceConfigValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e TrainingJobResourceConfigValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e TrainingJobResourceConfigValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e TrainingJobResourceConfigValidationError) ErrorName() string {
	return "TrainingJobResourceConfigValidationError"
}

// Error satisfies the builtin error interface
func (e TrainingJobResourceConfigValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sTrainingJobResourceConfig.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = TrainingJobResourceConfigValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = TrainingJobResourceConfigValidationError{}

// Validate checks the field values on TrainingJob with the rules defined in
// the proto definition for this message. If any rules are violated, an error
// is returned.
func (m *TrainingJob) Validate() error {
	if m == nil {
		return nil
	}

	if v, ok := interface{}(m.GetAlgorithmSpecification()).(interface{ Validate() error }); ok {
		if err := v.Validate(); err != nil {
			return TrainingJobValidationError{
				field:  "AlgorithmSpecification",
				reason: "embedded message failed validation",
				cause:  err,
			}
		}
	}

	if v, ok := interface{}(m.GetTrainingJobConfig()).(interface{ Validate() error }); ok {
		if err := v.Validate(); err != nil {
			return TrainingJobValidationError{
				field:  "TrainingJobConfig",
				reason: "embedded message failed validation",
				cause:  err,
			}
		}
	}

	return nil
}

// TrainingJobValidationError is the validation error returned by
// TrainingJob.Validate if the designated constraints aren't met.
type TrainingJobValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e TrainingJobValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e TrainingJobValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e TrainingJobValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e TrainingJobValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e TrainingJobValidationError) ErrorName() string { return "TrainingJobValidationError" }

// Error satisfies the builtin error interface
func (e TrainingJobValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sTrainingJob.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = TrainingJobValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = TrainingJobValidationError{}
