// Code generated by protoc-gen-validate. DO NOT EDIT.
// source: flyteidl/plugins/spark.proto

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
var _spark_uuidPattern = regexp.MustCompile("^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$")

// Validate checks the field values on SparkApplication with the rules defined
// in the proto definition for this message. If any rules are violated, an
// error is returned.
func (m *SparkApplication) Validate() error {
	if m == nil {
		return nil
	}

	return nil
}

// SparkApplicationValidationError is the validation error returned by
// SparkApplication.Validate if the designated constraints aren't met.
type SparkApplicationValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e SparkApplicationValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e SparkApplicationValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e SparkApplicationValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e SparkApplicationValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e SparkApplicationValidationError) ErrorName() string { return "SparkApplicationValidationError" }

// Error satisfies the builtin error interface
func (e SparkApplicationValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sSparkApplication.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = SparkApplicationValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = SparkApplicationValidationError{}

// Validate checks the field values on SparkJob with the rules defined in the
// proto definition for this message. If any rules are violated, an error is returned.
func (m *SparkJob) Validate() error {
	if m == nil {
		return nil
	}

	// no validation rules for ApplicationType

	// no validation rules for MainApplicationFile

	// no validation rules for MainClass

	// no validation rules for SparkConf

	// no validation rules for HadoopConf

	// no validation rules for ExecutorPath

	return nil
}

// SparkJobValidationError is the validation error returned by
// SparkJob.Validate if the designated constraints aren't met.
type SparkJobValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e SparkJobValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e SparkJobValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e SparkJobValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e SparkJobValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e SparkJobValidationError) ErrorName() string { return "SparkJobValidationError" }

// Error satisfies the builtin error interface
func (e SparkJobValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sSparkJob.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = SparkJobValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = SparkJobValidationError{}
