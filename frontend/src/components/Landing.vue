<template>
<div>
    <Slider/>
    <Subsection1/>
    <Subsection2/>
    <Subsection3/>
    <Footer/>
</div>
    
</template>

<script>
import Footer from '@/components/landing/Footer'
import Slider from '@/components/landing/Slider'
import Subsection1 from '@/components/landing/Subsection1'
import Subsection2 from '@/components/landing/Subsection2'
import Subsection3 from '@/components/landing/Subsection3'

export default {
    name: 'Landing',
    components: { Footer, Slider, Subsection1, Subsection2, Subsection3 },
    data() {
        return {
            //
        }
    }
}
</script>
