<template>
  <div>
    <section class="tm-margin-large-top">
      <div class="uk-container uk-text-center">
        <p
          class="uk-margin-remove-bottom tm-overtitle uk-margin-top uk-text-uppercase letter-spacing-l"
          data-uk-scrollspy="cls: uk-animation-slide-bottom-medium"
        >Welcome to Touchbase support</p>
        <h1
          class="uk-margin-small-top uk-heading-hero"
          data-uk-scrollspy="cls: uk-animation-slide-bottom-medium; delay: 40"
        >How can we help?</h1>

        <Categories />
      </div>
    </section>
    <PopularQuestions />
		<ContactUs />
		
  </div>
</template>

<script>
import Categories from "@/components/support/Categories"
import PopularQuestions from "@/components/support/PopularQuestions"
import ContactUs from "@/components/support/ContactUs"


export default {
  name: "Support",
  components: {
    Categories,
		PopularQuestions,
		ContactUs,
		
  }
};
</script>

<style>
</style>