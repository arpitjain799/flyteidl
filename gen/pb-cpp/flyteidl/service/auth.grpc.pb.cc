// Generated by the gRPC C++ plugin.
// If you make any local change, they will be lost.
// source: flyteidl/service/auth.proto

#include "flyteidl/service/auth.pb.h"
#include "flyteidl/service/auth.grpc.pb.h"

#include <functional>
#include <grpcpp/impl/codegen/async_stream.h>
#include <grpcpp/impl/codegen/async_unary_call.h>
#include <grpcpp/impl/codegen/channel_interface.h>
#include <grpcpp/impl/codegen/client_unary_call.h>
#include <grpcpp/impl/codegen/client_callback.h>
#include <grpcpp/impl/codegen/method_handler_impl.h>
#include <grpcpp/impl/codegen/rpc_service_method.h>
#include <grpcpp/impl/codegen/server_callback.h>
#include <grpcpp/impl/codegen/service_type.h>
#include <grpcpp/impl/codegen/sync_stream.h>
namespace flyteidl {
namespace service {

static const char* AuthMetadataService_method_names[] = {
  "/flyteidl.service.AuthMetadataService/GetOAuth2Metadata",
  "/flyteidl.service.AuthMetadataService/GetPublicClientConfig",
};

std::unique_ptr< AuthMetadataService::Stub> AuthMetadataService::NewStub(const std::shared_ptr< ::grpc::ChannelInterface>& channel, const ::grpc::StubOptions& options) {
  (void)options;
  std::unique_ptr< AuthMetadataService::Stub> stub(new AuthMetadataService::Stub(channel));
  return stub;
}

AuthMetadataService::Stub::Stub(const std::shared_ptr< ::grpc::ChannelInterface>& channel)
  : channel_(channel), rpcmethod_GetOAuth2Metadata_(AuthMetadataService_method_names[0], ::grpc::internal::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_GetPublicClientConfig_(AuthMetadataService_method_names[1], ::grpc::internal::RpcMethod::NORMAL_RPC, channel)
  {}

::grpc::Status AuthMetadataService::Stub::GetOAuth2Metadata(::grpc::ClientContext* context, const ::flyteidl::service::OAuth2MetadataRequest& request, ::flyteidl::service::OAuth2MetadataResponse* response) {
  return ::grpc::internal::BlockingUnaryCall(channel_.get(), rpcmethod_GetOAuth2Metadata_, context, request, response);
}

void AuthMetadataService::Stub::experimental_async::GetOAuth2Metadata(::grpc::ClientContext* context, const ::flyteidl::service::OAuth2MetadataRequest* request, ::flyteidl::service::OAuth2MetadataResponse* response, std::function<void(::grpc::Status)> f) {
  ::grpc::internal::CallbackUnaryCall(stub_->channel_.get(), stub_->rpcmethod_GetOAuth2Metadata_, context, request, response, std::move(f));
}

void AuthMetadataService::Stub::experimental_async::GetOAuth2Metadata(::grpc::ClientContext* context, const ::grpc::ByteBuffer* request, ::flyteidl::service::OAuth2MetadataResponse* response, std::function<void(::grpc::Status)> f) {
  ::grpc::internal::CallbackUnaryCall(stub_->channel_.get(), stub_->rpcmethod_GetOAuth2Metadata_, context, request, response, std::move(f));
}

void AuthMetadataService::Stub::experimental_async::GetOAuth2Metadata(::grpc::ClientContext* context, const ::flyteidl::service::OAuth2MetadataRequest* request, ::flyteidl::service::OAuth2MetadataResponse* response, ::grpc::experimental::ClientUnaryReactor* reactor) {
  ::grpc::internal::ClientCallbackUnaryFactory::Create(stub_->channel_.get(), stub_->rpcmethod_GetOAuth2Metadata_, context, request, response, reactor);
}

void AuthMetadataService::Stub::experimental_async::GetOAuth2Metadata(::grpc::ClientContext* context, const ::grpc::ByteBuffer* request, ::flyteidl::service::OAuth2MetadataResponse* response, ::grpc::experimental::ClientUnaryReactor* reactor) {
  ::grpc::internal::ClientCallbackUnaryFactory::Create(stub_->channel_.get(), stub_->rpcmethod_GetOAuth2Metadata_, context, request, response, reactor);
}

::grpc::ClientAsyncResponseReader< ::flyteidl::service::OAuth2MetadataResponse>* AuthMetadataService::Stub::AsyncGetOAuth2MetadataRaw(::grpc::ClientContext* context, const ::flyteidl::service::OAuth2MetadataRequest& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderFactory< ::flyteidl::service::OAuth2MetadataResponse>::Create(channel_.get(), cq, rpcmethod_GetOAuth2Metadata_, context, request, true);
}

::grpc::ClientAsyncResponseReader< ::flyteidl::service::OAuth2MetadataResponse>* AuthMetadataService::Stub::PrepareAsyncGetOAuth2MetadataRaw(::grpc::ClientContext* context, const ::flyteidl::service::OAuth2MetadataRequest& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderFactory< ::flyteidl::service::OAuth2MetadataResponse>::Create(channel_.get(), cq, rpcmethod_GetOAuth2Metadata_, context, request, false);
}

::grpc::Status AuthMetadataService::Stub::GetPublicClientConfig(::grpc::ClientContext* context, const ::flyteidl::service::PublicClientAuthConfigRequest& request, ::flyteidl::service::PublicClientAuthConfigResponse* response) {
  return ::grpc::internal::BlockingUnaryCall(channel_.get(), rpcmethod_GetPublicClientConfig_, context, request, response);
}

void AuthMetadataService::Stub::experimental_async::GetPublicClientConfig(::grpc::ClientContext* context, const ::flyteidl::service::PublicClientAuthConfigRequest* request, ::flyteidl::service::PublicClientAuthConfigResponse* response, std::function<void(::grpc::Status)> f) {
  ::grpc::internal::CallbackUnaryCall(stub_->channel_.get(), stub_->rpcmethod_GetPublicClientConfig_, context, request, response, std::move(f));
}

void AuthMetadataService::Stub::experimental_async::GetPublicClientConfig(::grpc::ClientContext* context, const ::grpc::ByteBuffer* request, ::flyteidl::service::PublicClientAuthConfigResponse* response, std::function<void(::grpc::Status)> f) {
  ::grpc::internal::CallbackUnaryCall(stub_->channel_.get(), stub_->rpcmethod_GetPublicClientConfig_, context, request, response, std::move(f));
}

void AuthMetadataService::Stub::experimental_async::GetPublicClientConfig(::grpc::ClientContext* context, const ::flyteidl::service::PublicClientAuthConfigRequest* request, ::flyteidl::service::PublicClientAuthConfigResponse* response, ::grpc::experimental::ClientUnaryReactor* reactor) {
  ::grpc::internal::ClientCallbackUnaryFactory::Create(stub_->channel_.get(), stub_->rpcmethod_GetPublicClientConfig_, context, request, response, reactor);
}

void AuthMetadataService::Stub::experimental_async::GetPublicClientConfig(::grpc::ClientContext* context, const ::grpc::ByteBuffer* request, ::flyteidl::service::PublicClientAuthConfigResponse* response, ::grpc::experimental::ClientUnaryReactor* reactor) {
  ::grpc::internal::ClientCallbackUnaryFactory::Create(stub_->channel_.get(), stub_->rpcmethod_GetPublicClientConfig_, context, request, response, reactor);
}

::grpc::ClientAsyncResponseReader< ::flyteidl::service::PublicClientAuthConfigResponse>* AuthMetadataService::Stub::AsyncGetPublicClientConfigRaw(::grpc::ClientContext* context, const ::flyteidl::service::PublicClientAuthConfigRequest& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderFactory< ::flyteidl::service::PublicClientAuthConfigResponse>::Create(channel_.get(), cq, rpcmethod_GetPublicClientConfig_, context, request, true);
}

::grpc::ClientAsyncResponseReader< ::flyteidl::service::PublicClientAuthConfigResponse>* AuthMetadataService::Stub::PrepareAsyncGetPublicClientConfigRaw(::grpc::ClientContext* context, const ::flyteidl::service::PublicClientAuthConfigRequest& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderFactory< ::flyteidl::service::PublicClientAuthConfigResponse>::Create(channel_.get(), cq, rpcmethod_GetPublicClientConfig_, context, request, false);
}

AuthMetadataService::Service::Service() {
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      AuthMetadataService_method_names[0],
      ::grpc::internal::RpcMethod::NORMAL_RPC,
      new ::grpc::internal::RpcMethodHandler< AuthMetadataService::Service, ::flyteidl::service::OAuth2MetadataRequest, ::flyteidl::service::OAuth2MetadataResponse>(
          std::mem_fn(&AuthMetadataService::Service::GetOAuth2Metadata), this)));
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      AuthMetadataService_method_names[1],
      ::grpc::internal::RpcMethod::NORMAL_RPC,
      new ::grpc::internal::RpcMethodHandler< AuthMetadataService::Service, ::flyteidl::service::PublicClientAuthConfigRequest, ::flyteidl::service::PublicClientAuthConfigResponse>(
          std::mem_fn(&AuthMetadataService::Service::GetPublicClientConfig), this)));
}

AuthMetadataService::Service::~Service() {
}

::grpc::Status AuthMetadataService::Service::GetOAuth2Metadata(::grpc::ServerContext* context, const ::flyteidl::service::OAuth2MetadataRequest* request, ::flyteidl::service::OAuth2MetadataResponse* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status AuthMetadataService::Service::GetPublicClientConfig(::grpc::ServerContext* context, const ::flyteidl::service::PublicClientAuthConfigRequest* request, ::flyteidl::service::PublicClientAuthConfigResponse* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}


}  // namespace flyteidl
}  // namespace service

