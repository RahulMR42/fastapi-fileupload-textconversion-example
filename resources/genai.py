import oci

class Genai:
    def __init__(self, compartment_ocid):
        self.compartment_ocid = compartment_ocid

    def summerise_text(self, text_to_summerise):

        CONFIG_PROFILE = "DEFAULT"
        config = oci.config.from_file('~/.oci/config', CONFIG_PROFILE)
        endpoint = "https://inference.generativeai.us-chicago-1.oci.oraclecloud.com"
        generative_ai_inference_client = oci.generative_ai_inference.GenerativeAiInferenceClient(config=config, service_endpoint=endpoint, retry_strategy=oci.retry.NoneRetryStrategy(), timeout=(10,240))
        text_to_summarize = text_to_summerise
        summarize_text_detail = oci.generative_ai_inference.models.SummarizeTextDetails()
        summarize_text_detail.serving_mode = oci.generative_ai_inference.models.OnDemandServingMode(model_id="cohere.command")
        summarize_text_detail.compartment_id = "ocid1.compartment.oc1..aaaaaaaakp7cug2a5zpyl5sz6tnxvqlfw7hzaxc77fqovimxfk4f4ricz7kq"
        summarize_text_detail.input = text_to_summarize
        summarize_text_detail.additional_command = ""
        summarize_text_detail.extractiveness = "HIGH"
        summarize_text_detail.format = "AUTO"
        summarize_text_detail.length = "AUTO"
        summarize_text_detail.temperature = 1
        summarize_text_response = generative_ai_inference_client.summarize_text(summarize_text_detail)
        # Print result
        return(summarize_text_response.data)