<template>
  <div class="uk-margin-large-top uk-section-primary">
    <div class="uk-container">
      <hr class="uk-margin-remove" />
      <div
        class="uk-grid-large uk-flex-middle uk-margin-xlarge-top uk-margin-xlarge-bottom"
        data-uk-grid
        data-uk-scrollspy="cls: uk-animation-slide-bottom; repeat: true"
      >
        <div class="uk-width-auto@m">
          <p class="uk-text-large">Didn't find an answer to your question?</p>
        </div>
        <div class="uk-width-expand@m">
					<router-link to="/contact">
						<a class="tm-button uk-link tm-button-xlarge" >Contact Us</a>
					</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>